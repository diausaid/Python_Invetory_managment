
def update_product(inventory_managers):
    product_id = input("Enter the product ID of the product to be updated: ")
    name = input("Enter the new name for the product: ")
    price = input("Enter the new price for the product: ")
    quantity = input("Enter the new quantity for the product: ")

    inventory_managers.update_product(product_id, name, price, quantity)

