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