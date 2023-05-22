import pytest

from src.phone import Phone
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def get_digit_in_string():
    return '5'

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def phone2():
    phone2 = Phone("iPhone 13", 100_000, 5, 2)
    return phone2

@pytest.fixture
def kb1():
    return Keyboard('Dark Project KD87A', 9600, 5)
