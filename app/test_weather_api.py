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
    
    if response.status_code != 200:
        raise Exception("API call failed")
    
    return response.json()

# Test for a function
def test_get_weather_data():
    city = "London"
    data = get_weather_data(city)
    return data

if __name__ == "__main__":
    print(test_get_weather_data())