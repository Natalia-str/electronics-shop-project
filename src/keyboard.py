from src.item import Item

class Keyboard(Item, MixinLang):
    def __init__(self, name: str, price: float, quantity: int, language: str) -> None:
        """
            Создание экземпляра класса keyboard.

            :param name: Название товара.
            :param price: Цена за единицу товара.
            :param quantity: Количество товара в магазине.
            :param language: Язык раскладки.
            """
        super().__init__(name, price, quantity)
        self.__language = language


class MixinLang:
    language = "EN"
    def change_lang(self, language):
        if language == "EN":
            language = "RU"
            return language
        elif language == "RU":
            language = "EN"
            return language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

