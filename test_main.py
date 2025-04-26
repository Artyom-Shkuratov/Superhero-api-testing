import pytest
import requests
from main import get_tallest_hero_by_gender_and_work

# Проверка корректного возврата имени самого высокого героя
def test_get_response_satus_code_is_200():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize("gender, has_work", [
    ("Male", True),
    ("Male", False),
    ("Female", True),
    ("Female", False),
])

def test_get_tallest_hero_returns_valid_name(gender, has_work):
    hero = get_tallest_hero_by_gender_and_work(gender, has_work)
    if hero is not None:
        assert isinstance(hero, str)
        assert len(hero) > 0
    else:
        assert hero is None
        
def test_height_list_short_returns_none():
    result = get_tallest_hero_by_gender_and_work("Genderless", True)
    assert result is None
    
def test_empty_height_string_returns_none():
    result = get_tallest_hero_by_gender_and_work("EmptyHeight", True)
    assert result is None

# Проверка, что не падает при передаче несуществующего пола
def test_invalid_gender_returns_none():
    result = get_tallest_hero_by_gender_and_work("UnknownGender", True)
    assert result is None

# Проверка, что не падает при передаче цифр вместо строки
def test_number_instead_of_gender_returns_none():
    result = get_tallest_hero_by_gender_and_work(12345, True)
    assert result is None

# Проверка, что при пустом значении пола результат None
def test_empty_gender_returns_none():
    result = get_tallest_hero_by_gender_and_work("", True)
    assert result is None


def test_invalid_gender_returns_none():
    assert get_tallest_hero_by_gender_and_work("Unknown", True) is None

def test_non_boolean_has_job_returns_none():
    assert get_tallest_hero_by_gender_and_work("Male", "yes") is None

def test_null_gender_returns_none():
    assert get_tallest_hero_by_gender_and_work('', "yes") is None
