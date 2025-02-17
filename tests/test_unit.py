import pytest
from app.utils import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(3, 3) == 6