import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def get_digit_in_string():
    return '5'

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

# @pytest.fixture
# def phone2():
#     phone2 = Phone("iPhone 14", 120_000, 5, 2)
#     return phone2

# @pytest.fixture
# def item_2():
#     return Item