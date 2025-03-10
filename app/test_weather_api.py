import requests
import pytest
import os 
from dotenv import load_dotenv

load_dotenv()

# Load the API keys from the .env file
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# A function that makes an API call to WeatherAPI
def get_weather_data(city):
    api_key = WEATHER_API_KEY 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    response_json = response.json()
    if "error" in response_json:
        error_code = response_json["error"]["code"]

        if error_code == 1006:
            raise ValueError("City not found")
        elif error_code == 1002:
            raise KeyError("API key is invalid")
        else:
            raise Exception(f"API call failed: {response_json['error']['message']}")

    return response.json()

# Test for a function
def test_get_weather_data():
    city = "London"
    data = get_weather_data(city)
    return data

if __name__ == "__main__":
    print(test_get_weather_data())