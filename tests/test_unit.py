import pytest
from app.utils import add_numbers, average_temperature, temperature_difference

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(3, 3) == 6

# Test for average_temperature function
def test_average_temperature():
    assert average_temperature(2, 3) == 2.5
    assert average_temperature(3, 3) == 3

# Test for temperature_difference function
def test_temperature_difference():
    assert temperature_difference(2, 3) == 1
    assert temperature_difference(3, 3) == 0