
from .product import Product

def add_product(inventory_managers,product_id):
    
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        product=Product(product_id,product_name,price,quantity)

        inventory_managers.add_product(product,product_id)


