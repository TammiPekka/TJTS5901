import requests
import pytest
from unittest.mock import patch
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# An example of a function that makes an API call
def get_weather_data(city):
    api_key = WEATHER_API_KEY  # Use the API key from the environment variable
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("API call failed")
    
    return response.json()

# Test for a function
@patch('requests.get')
def test_get_weather_data(mock_get):
    city = "London"
    mock_response = {
        "location": {"name": city},
        "current": {"temp_c": 15.0}
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    data = get_weather_data(city)

    # Assertions to verify the correctness of the data
    assert "location" in data
    assert "current" in data
    assert data["location"]["name"] == city
    assert "temp_c" in data["current"]
    assert data["current"]["temp_c"] == 15.0

if __name__ == "__main__":
    print(test_get_weather_data())