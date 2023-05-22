def test_phone_init(phone1):
    """ Проверка инициализации класса"""
    assert phone1.name == 'iPhone 14'
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test__repr__(phone1):
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test__str__(phone1):
    assert str(phone1) == 'iPhone 14'
    assert phone1.__str__() == 'iPhone 14'

def test__add__(phone1, phone2):
    """Проверка сложения объектов классов"""
    assert phone1 + phone2 == 10

