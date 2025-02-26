import pytest
import requests
from app.test_weather_api import get_weather_data
from app.api_openw import get_open_data
from app.app import app

BASE_URL = "http://localhost:5001"  
BASE_URL_WEATHER = "http://api.openweathermap.org/data/2.5/weather"

#Testing basic functionality of the app
def test_home():
    """Test if home endpoint is reachable"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

#Testing weather api functionality
def test_weather_api_ok():
 # Make an API request and store the response in 'data'
    city = "London"
    data = get_weather_data(city)  # Converts the JSON response into a Python dictionary to be used in the tests
    # Test that the returned data contains the necessary information from WeatherAPI
    assert "location" in data  # Ensures that 'location' information is present in the returned data
    assert "current" in data  # Ensures that 'current' information is present, which includes the current weather data
    assert data["location"]["name"] == city  # Ensures that the returned city matches the input city
    assert "temp_c" in data["current"]  # Ensures that the data includes the temperature ('temp_c') in the current weather details


#Testing open weather api functionality
def test_open_api_ok():
 # Make an API request and store the response in 'data'
    city = "London"
    data = get_open_data(city)  # Converts the JSON response into a Python dictionary to be used in the tests
    # Test that the returned data contains the necessary information from OpenWeatherMap API
    assert "main" in data  # Ensures that 'main' information is present in the returned data
    assert "temp" in data["main"]  # Ensures that the data includes the temperature ('temp') in the main weather details
    assert "name" in data  # Ensures that 'name' information is present in the returned data
    assert data["name"] == city  # Ensures that the returned city matches the input
    