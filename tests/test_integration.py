import pytest
from unittest.mock import patch
from app.test_weather_api import get_weather_data

@patch('requests.get')
def test_weather_api_ok(mock_get):
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