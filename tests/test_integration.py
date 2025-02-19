import pytest
import requests

BASE_URL = "http://localhost:5000"  

def test_home():
    """Test if home endpoint is reachable"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

 # Make an API request and store the response in 'data'
    data = response.json()  # Converts the JSON response into a Python dictionary to be used in the tests

    # Define the city to check against
    city = "Helsinki"  # Replace with the city you want to test

    # Test that the returned data contains the necessary information from WeatherAPI
    assert "location" in data  # Ensures that 'location' information is present in the returned data
    assert "current" in data  # Ensures that 'current' information is present, which includes the current weather data
    assert data["location"]["name"] == city  # Ensures that the returned city matches the input city
    assert "temp_c" in data["current"]  # Ensures that the data includes the temperature ('temp_c') in the current weather details


# Tests for OpenWeatherAPI integration

# Test that API returns right temperature for Helsinki
def test_get_temperature_success():
    city = "Helsinki"
    response = requests.post(f"{BASE_URL}/get_temperature", data={"city": city})
    data = response.json()
    assert response.status_code == 200
    assert "temperature1" in data
    assert isinstance(data["temperature1"], (int, float))  # Tarkistaa, että lämpötila on numero

# Test that the API returns an error message if the city is missing
def test_get_temperature_missing_city():
    response = requests.post(f"{BASE_URL}/get_temperature", data={})
    data = response.json()
    assert response.status_code == 400
    assert data["error"] == "City is required"

# Test that the API returns an error message if the city is invalid
def test_get_temperature_invalid_city():
    city = "InvalidCityName123"
    response = requests.post(f"{BASE_URL}/get_temperature", data={"city": city})
    data = response.json()
    assert response.status_code == 404
    assert "error" in data
