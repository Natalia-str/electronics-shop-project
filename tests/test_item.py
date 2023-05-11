"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test_item_calculate_total_price(item1):
    """Проверка стоимости позиции всего товара в магазине"""
    assert item1.calculate_total_price() == 200000


def test_item_apply_discount(item1):
    """Проверка применения скидки к цене"""
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 8000.0

def test_item_init(item1):
    """ Проверка инициализации класса"""
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_string_to_number(get_digit_in_string):
    assert Item.string_to_number(get_digit_in_string) == 5


def test_instantiate_from_csv(item_2):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

