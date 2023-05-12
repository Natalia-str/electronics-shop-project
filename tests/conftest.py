import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def get_digit_in_string():
    return '5'

# @pytest.fixture
# def item_2():
#     return Item