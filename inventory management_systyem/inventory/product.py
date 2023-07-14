class Product:
    def __init__(self, ID, name, price, quantity):
        self.ID = ID
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    def set_product(self,id, name,price,quantity):
        self.ID = id
        self.name = name
        self.price =price
        self.quantity = quantity

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
         return f"ID: {self.ID}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
# product = Product(1, "laptop", 900, 3)
# print(product)
# print(product.__str__())