import requests
import pytest
import os 
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")

url_weather = "http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
url_open = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# An example of a function that makes an API call
def get_weather_data(api_key, url_template, city):
    url = url_template.format(api_key=api_key, city=city)
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("API call failed")
    
    data = response.json()
    data1 = data #for testing purposes

    if "current" in data:  # WeatherAPI
        return data["current"]["temp_c"]
    elif "main" in data:  # OpenWeather
        return data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
    else:
        raise Exception("Invalid response format")

    

# Test for a function
def test_get_weather_data():
    city = "London"
    weather_data = get_weather_data(WEATHER_API_KEY, url_weather, city)
    openweather_data = get_weather_data(OPEN_W_API_KEY, url_open, city)
    return weather_data, openweather_data

if __name__ == "__main__":
    weather_data, openweather_data = test_get_weather_data()
    print("WeatherAPI data:", weather_data)
    print("OpenWeather data:", openweather_data)
    