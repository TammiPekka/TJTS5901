import pytest
import requests

BASE_URL = "http://localhost:5000"  

def test_home():
    """Test if home endpoint is reachable"""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
