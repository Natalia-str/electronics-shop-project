import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    path = '/Users/natalia/electronic_shop/src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return self.__name

    def __add__(self, other):
        # return self.quantity + other.quantity
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """ сеттер name проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(name) > 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = name


    @staticmethod
    def string_to_number(arg):
        """статический метод, возвращающий число из числа-строки"""
        numb = int(float(arg))
        return numb


    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""
        cls.all.clear()
        with open(cls.path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if csvfile is None:
                raise ModuleNotFoundError('Отсутствует файл item.csv')
            else:
                for row in reader:
                    # print(row)
                    cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))
                # print(cls.all)
                return cls.all


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

# item1 = Item("Смартфон", 10000, 20)
# item_1 = Item("Petr Petrov", 10000, 3)
# print(item_1.all)
# item_1.instantiate_from_csv()
# item1 = Item.all[0]
# print(item1)
# print(item1.calculate_total_price())
# print(item1.__repr__())