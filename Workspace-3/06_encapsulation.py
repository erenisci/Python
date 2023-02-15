class Product:
    def __init__(self):
        self.__price = 1000

    def print_price(self):
        print(f"Product price: {self.__price}")

    def set_price(self, price):
        self.__price = price


p = Product()
p.print_price()

p.__price = 999
p.print_price()

p.set_price(500)
p.print_price()
