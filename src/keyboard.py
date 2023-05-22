from src.item import Item
from src.mixinlang import MixinLang

class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
            Создание экземпляра класса keyboard.

            :param name: Название товара.
            :param price: Цена за единицу товара.
            :param quantity: Количество товара в магазине.
            """
        super().__init__(name, price, quantity)

# kb = Keyboard('Dark Project KD87A', 9600, 5)
# print(str(kb))
# print(str(kb.language))
# kb.change_lang()
# print(str(kb.language))
# kb.change_lang().change_lang()
# print(str(kb.language))