import requests
import pytest
import os 
from dotenv import load_dotenv

load_dotenv()

# Load the API keys from the .env file
OPEN_W_API_KEY = os.getenv("OPEN_W_API_KEY")


# Function to get weather data from openweathermap API with city name
def get_open_data(city):
    api_key = OPEN_W_API_KEY 
    url_open = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url_open, timeout=5)
    
    #Catch errors
    if response.status_code == 404:
        raise ValueError("City not found")
    
    if response.status_code == 401:
        raise KeyError("API key is invalid")
    
    if response.status_code != 200:
        raise Exception("API call failed")

    return response.json()


# This is to get weather data fron same location as weatherAPI, because there is many cities with same name around the world

def get_open_datalat(lat, lon):
    api_key = OPEN_W_API_KEY 
    url_open = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url_open, timeout=5)
    
    #Catch errors
    if response.status_code == 404:
        raise ValueError("City not found")
    
    if response.status_code == 401:
        raise KeyError("API key is invalid")
    
    if response.status_code != 200:
        raise Exception("API call failed")

    return response.json()


# Test for a function
def test_get_open_data():
    city = "London"
    data = get_open_data(city)
    return data

if __name__ == "__main__":
    print(test_get_open_data())