import requests
import pytest

# An example of a function that makes an API call
def get_weather_data(city):
    api_key = "994994fe63a749f181e101136251702"  # korvaa tämä WeatherAPI:n API-avaimella
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("API call failed")
    
    return response.json()

# Test for a function
def test_get_weather_data():
    city = "London"
    data = get_weather_data(city)
    
<<<<<<< HEAD
=======
    # Testaa, että saatu data sisältää tarvittavat tiedot
    assert "location" in data
    assert "current" in data
    assert data["location"]["name"] == city  # Varmistaa, että kaupunki on sama kuin syötteessä
    assert "temp_c" in data["current"]  # Varmistaa, että lämpötila on mukana
>>>>>>> starter-UI
