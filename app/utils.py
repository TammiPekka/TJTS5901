def add_numbers(a, b):
    return a + b

## tänne voisi tehdä lisää testejä, esim. testataan että funktio toimii myös negatiivisilla luvuilla
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(3, 3) == 6
    assert add_numbers(-2, 3) == 1
    assert add_numbers(-3, -3) == -6
    assert add_numbers(0, 0) == 0