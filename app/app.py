import sys
from flask import Flask
from flask import render_template, request, jsonify
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

@app.route("/")
def home():
    nimi = "Jukka"
    city = request.args.get("city", "")

    #if "city" in request.args:
    #    city = request.args["city"]

    temperature_weather = None
    temperature_open = None
    avg = None
    dif = None

    if city:
        # Get weather data from WeatherAPI
        data_weather = get_weather_data(city)
        # Extract the temperature from the data
        temperature_weather = data_weather["current"]["temp_c"]
        # Get weather data from OpenWeatherMap API
        data_open = get_open_data(city)
        # Extract the temperature from the data
        temperature_open = round(data_open["main"]["temp"] - 273.15, 2)
        # Count average of two temperatures
        avg = round(average_temperature(temperature_weather, temperature_open), 3)
        # Return difference between two temperatures
        dif = round(temperature_difference(temperature_weather, temperature_open), 3)

    # Render the home.html template with the data
    return render_template("home.html", nimi=nimi, city=city, temperature_weather=temperature_weather, temperature_open=temperature_open, avg=avg, dif=dif)

@app.route("/home")
def health():
    return "OK"

@app.route("/testing")
def tester():
    return "testing endpoint, aasd,asdf,asd, test"


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
    app.run(host="0.0.0.0", port=5001)