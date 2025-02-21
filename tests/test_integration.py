import pytest
import requests
from app.test_weather_api import get_weather_data
from app.app import app

BASE_URL = "http://localhost:5000"  
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



#========Below are tests for open weather API=========
#test client to test the API calls and the responses
@pytest.fixture
def client():
   app.config["TESTING"] = True
   with app.test_client() as client:
       yield client

# Test that API returns right temperature for Helsinki
def test_get_temperature_success(client, mocker):
   mock_response = {"main": {"temp": 22.5}}  # Mocked API response
   # Mock the requests.get call to prevent real API calls
   mocker.patch("requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

   response = client.get("/get_temperature?city=London")
   data = response.get_json()
   assert response.status_code == 200
   assert "temperature1" in data
   assert isinstance(data["temperature1"], (int, float))


# Test that the API returns an error message if the city is missing
def test_get_temperature_missing_city(client):
    response = client.get("/get_temperature")  # No city parameter
    data = response.get_json()
    assert response.status_code == 400
    assert "error" in data
    assert data["error"] == "City is required"

# Test that the API returns an error message if the city is invalid
def test_get_temperature_invalid_city(client, mocker):
    mock_response = {"message": "city not found"}  # Mock API response for invalid city
    # Mock the requests.get call to return a 404 error
    mocker.patch("requests.get", return_value=mocker.Mock(status_code=404, json=lambda: mock_response))

    response = client.get("/get_temperature?city=InvalidCityName123")
    data = response.get_json()
    assert response.status_code == 404
    assert "error" in data
    assert data["error"] == "city not found"