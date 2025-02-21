import pytest
from app.utils import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(3, 3) == 6

## Jokaiselle keskeiselle koodiosalle olisi hyvä tehdä testit. Tässä tapauksessa testataan add_numbers-funktiota, joka on yksi sovelluksen keskeisistä osista. Testit varmistavat, että funktio toimii odotetulla tavalla ja palauttaa oikeat arvot. Tämä auttaa varmistamaan sovelluksen toimivuuden ja vähentää virheiden riskiä. Testit myös auttavat kehittäjää ymmärtämään, miten koodi toimii ja miten sitä voidaan parantaa. Testien avulla voidaan myös helposti havaita, jos jokin muutos koodissa rikkoo jotain toiminnallisuutta. Testien kirjoittaminen on siis tärkeä osa ohjelmistokehitystä ja auttaa varmistamaan sovelluksen laadun ja toimivuuden.