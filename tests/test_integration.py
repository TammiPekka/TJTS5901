import pytest
import requests
import os 
from app.test_weather_api import get_weather_data
from app.app import app

BASE_URL = "http://localhost:5001"  

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")

url_weather = "http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
url_open = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

#Testing basic functionality of the app
def test_home():
    """Test if home endpoint is reachable"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

#Testing weather api functionality
def test_weather_api_ok():
 # Make an API request and store the response in 'data'
    city = "London"
    data = get_weather_data(WEATHER_API_KEY, url_weather, city)  # Converts the JSON response into a Python dictionary to be used in the tests
    # Test that the returned data contains the necessary information from WeatherAPI
    assert isinstance(data, float)  # Ensure the temperature is a float
