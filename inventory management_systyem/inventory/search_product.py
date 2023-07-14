# from inventory import inventory_manager
# from inventory import product
def search_product(inventory_manager):
    search_by = input("Enter 1  to search by ID or 2 to search by name: ")
    search_term = input("Enter the ID or name of the product to be searched: ")

    if search_by == "1":
        product = inventory_manager.search_product_by_id(search_term)
    else:
        product = inventory_manager.search_product_by_name(search_term)

    if product is not None:
        print(f"Product found: {product}")
    else:
        print("Product not found.")

    # inventory/search_product.py

# from .inventory_manager import InventoryManager

# inventory_manager = InventoryManager()
# product = inventory_manager.search_product("product1")
# print(f"Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")


