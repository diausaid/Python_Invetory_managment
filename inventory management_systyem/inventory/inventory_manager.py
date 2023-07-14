# inventory/inventory_manager.py

from .product import Product
class InventoryManager:
    def __init__(self):
        self.products = []

    def add_product(self, product,id) : 
         if  self.products :

             for produc in self.products:
                if produc.ID == id :
                    print("product already exist ")
                    return 
        
             
             

       
         self.products.append(product)
         print("Product added successfully.")  
   


                    
               
    

    def remove_product(self, name):
        if  self.products :
            
              for product in self.products:
                 if product.name == name:
                  self.products.remove(product)
                  print(f"{product} is successfully removed ")

        else:
            print("there is no products")

    def update_product(self,ID , name=None, quantity=None, price=None):
        if  self.products :
            for product in self.products:
                if product.name == name or product.ID == ID:

                        
                    if quantity is not None:
                        product.name =name
                        product.quantity = quantity
                    if price is not None:
                        product.price = price
                    print("successfully updated")
                else:
                    print("product doesn't exist ")
        else:
            print("there is no products")
                

    def search_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product

    def search_product_by_id(self, id):
        for product in self.products:
            if product.ID == id:
                return product
    def display_products(self):
        if not self.products:
            print("no product to display")
        else:
            for product in self.products:
                print(f" ID: {product.ID} Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}")
    def __str__(self):
         return f"products {self.products}"