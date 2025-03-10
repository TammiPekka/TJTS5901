import sys
from flask import Flask
from flask import render_template, request, jsonify, session
import requests
import jinja2
import os
from dotenv import load_dotenv

sys.path.append("app")
from utils import average_temperature, temperature_difference
from test_weather_api import get_weather_data
from api_openw import get_open_data

app = Flask(__name__)
load_dotenv()

# Load the API keys from the .env file
OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
app.secret_key = os.getenv("SECRET_KEY") 
#TODO: handle when input is invalid city or empty

@app.route("/")
def home():
    city = ""

    temperature_weather = None
    temperature_open = None
    avg = None
    dif = None
    #Search history, save result to session
    if "search_history" not in session:
        session["search_history"] = []
    search_history = session.get("search_history", [])
    # Get the city from the input field
    city = request.args.get("city", "")
    #if city is empty:
    if city == "":
        return render_template("home.html", city="Enter city", temperature_weather="", temperature_open="", avg="", dif="", search_history=search_history)
    #if city is not "":
    if city:
        # Try to get the weather data from the API, if there is a connection error, return an error message
        try:
            # Get weather data from WeatherAPI, if there is a connection error put error message in temperature_weather
            data_weather = get_weather_data(city)
            # Extract the temperature from the data
            temperature_weather = data_weather["current"]["temp_c"]
        # Catch the exceptions
        except ValueError as e:
            temperature_weather = "City not found"
        except KeyError as e:
            temperature_weather = "API key is invalid"
        except Exception as e:
            temperature_weather = "Connection error with API"

        try:
            # Get weather data from OpenWeatherMap API, if there is a connection error put error message in temperature_open
            data_open = get_open_data(city)
            # Extract the temperature from the data
            temperature_open = round(data_open["main"]["temp"] - 273.15, 2) # Convert temperature from Kelvin to Celsius #TODO check if there is better way to chance kelvin to celsius
        # Catch the exceptions
        except ValueError as e:
            temperature_open = "City not found"
        except KeyError as e:
            temperature_open = "API key is invalid"
        except Exception as e:
            temperature_open = "Connection error with API"

        # If both API calls return City not found, city is not found
        if temperature_weather == "City not found" and temperature_open == "City not found":
            city = "City not found"
            return render_template("home.html", city=city, temperature_weather="-", temperature_open="-", avg="-", dif="-", search_history=search_history)  
    
        # If temperature_weathet in not a number, return the OpenWeatherMap temperature as the average for search history
        try:
            temperature_weather = float(temperature_weather)
        except (ValueError, TypeError):
            avg = temperature_open
            dif = ""
            return render_template("home.html", city=city, temperature_weather=temperature_weather, temperature_open=temperature_open, avg=avg, dif=dif, search_history=search_history)
        # If temperature_open in not a number, return the WeatherAPI temperature as the average for search history
        try:
            temperature_open = float(temperature_open)
        except (ValueError, TypeError):
            avg = temperature_weather
            dif = ""
            return render_template("home.html", city=city, temperature_weather=temperature_weather, temperature_open=temperature_open, avg=avg, dif=dif, search_history=search_history)

        else:    
            # Count average of two temperatures
            avg = round(average_temperature(temperature_weather, temperature_open), 3)
            # Return difference between two temperatures
            dif = round(temperature_difference(temperature_weather, temperature_open), 3)
            # Render the home.html template with the data

                        #store the seacrch history

            if city:
                session["search_history"].insert(0, 
                                        {"city":city,
                                        "temperature_weather":temperature_weather,
                                        "temperature_open":temperature_open, 
                                        "avg":avg,
                                        "dif":dif
                })
                session.modified = True


            # Render the home.html template with the data
            return render_template("home.html", 
                                city=city, 
                                temperature_weather=temperature_weather, 
                                temperature_open=temperature_open, 
                                avg=avg, 
                                dif=dif,
                                search_history=search_history)

            #return render_template("home.html", nimi=nimi, city=city, temperature_weather=temperature_weather, temperature_open=temperature_open, avg=avg, dif=dif)
    

    #store the seacrch history
    if "search_history" not in session:
        session["search_history"] = []
    if city:
        session["search_history"].insert(0, 
                                {"city":city,
                                 "temperature_weather":temperature_weather,
                                 "temperature_open":temperature_open, 
                                 "avg":avg,
                                 "dif":dif
        })
        session.modified = True

    search_history = session.get("search_history", [])
    print(search_history)

    # Render the home.html template with the data
    return render_template("home.html", 
                           city=city, 
                           temperature_weather=temperature_weather, 
                           temperature_open=temperature_open, 
                           avg=avg, 
                           dif=dif,
                           search_history=search_history)

@app.route("/home")
def health():
    return "OK"

@app.route("/clear_history", methods=["POST"])
def clear_history():
    session["search_history"] = []
    session.modified = True
    return "", 204

@app.route("/get_cities")
def get_cities():
    query = request.args.get("q", "")
    #query = "hel"
    if not query:
        return jsonify([])

    api_url = f"https://api.weatherapi.com/v1/search.json?key={WEATHER_API_KEY}&q={query}"
    response = requests.get(api_url)

    if response.status_code == 200:
        cities = response.json()
        suggestions = [{"name": city["name"], "country": city["country"]} for city in cities[:5]]
        return jsonify(suggestions)
    
    return jsonify([]), 500  # Return empty list on failure


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)