"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


Item.pay_rate = 0.8

def test_item_calculate_total_price(item1):
    """Проверка стоимости позиции всего товара в магазине"""
    assert item1.calculate_total_price() == 200000


def test_item_apply_discount(item1):
    """Проверка применения скидки к цене"""
    assert item1.apply_discount() == 8000.0

def test_item_init(item1):
    """ Проверка инициализации класса"""
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20