import inventory
def main():
 print("   Inventory Management System ")
 print("------------------------")
        
 try:
    n = int(input(" 1. Add Product\n 2. Update Product\n 3. Search Product by Name \n 4. Remove Product \n 5. Display All Products \n  6. Exit \n enter your number "))
    if n > 6 :
        print("please enter values '1' to '6' ")

    inv= inventory.InventoryManager()

    while n in range(1,7):
            
            

            if n==1:
            
                product_id = input("Enter product ID: ")
            
                inventory.add_product(inv,product_id)

            elif n==2:
                inventory.update_product(inv)

            elif n==3:
                inventory.search_product(inv)

            elif n==4:
                inventory.remove_product(inv)

            elif n==5:
                inventory.display_product(inv)
                
            elif n==6:
                print("program exiting------")
                return
            n = int(input(" 1. Add Product\n 2. Update Product\n 3. Search Product by Name \n 4. Remove Product \n 5. Display All Products \n  6. Exit \n enter your number "))

 except ValueError:
     print("please enter values '1' to '6' ")
     main()



   
 

if __name__ == "__main__":
  main()