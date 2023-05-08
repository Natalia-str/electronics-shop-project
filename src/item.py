import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    # csv_path = '/Users/natalia/electronic_shop/src/items.csv'

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
        self.all.append(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            print("Длина наименования товара превышает 10 символов")
        else:
            self.__name = name
    @staticmethod
    def string_to_number(arg):
        numb = int(arg)
        return numb

    @classmethod
    def instantiate_from_csv(cls):
        csv_path = '/Users/natalia/electronic_shop/src/items.csv'
        with open(csv_path, encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = Item(row['name'], row['price'], row['quantity'])
                return item


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
