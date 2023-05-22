def test_keyboard_init(kb1):
    """ Проверка инициализации класса"""
    assert kb1.name == 'Dark Project KD87A'
    assert kb1.price == 9600
    assert kb1.quantity == 5
    assert kb1.language == "EN"
    kb1.language == "CH"
    assert kb1.language == "EN"


def test_change_lang(kb1):
    kb1.change_lang()
    assert str(kb1.language) == "RU"

