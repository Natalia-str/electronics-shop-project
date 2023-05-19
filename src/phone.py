from item import Item

class Phone(Item):
    """
        Класс для представления телефонов в магазине.
        """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
                Создание экземпляра класса phone.

                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :param number_of_sim: Количество сим-карт.
                """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim == 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"




    def __add__(self, other):
        """сложение экземпляров класса Phone и Item (сложение по количеству товара в магазине)"""
        if isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)
print(item1 + phone1)
phone1.number_of_sim = 0