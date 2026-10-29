import json


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        
    def find_product(self, inventory, product_id):
        for product in inventory:
            if product['id'].lower() == product_id.lower():
                return product
        return None

    def update_stock(self, inventory, product_id, new_stock):
        product = self.find_product(inventory, product_id)
        if product == None:
            print("Product is not found.")
            return
        product['stock'] = new_stock
        print("Product stock updated successfully.")
    

class Inventory:
    def __init__(self):
        self.__products = []
    
    def add_product(self, inventory, product_id, name, price, stock):
            if find_product(inventory,product_id):
                print("Product ID already exists.")
                return
            inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
            print("Product added successfully!")
    
    def search_product(self, inventory, product_id):
        product=find_product(inventory, product_id)
        if product == None:
            print("Product is not found.")
            return
        print("Product Found")
        print("-" * 50)
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Stock: {product['stock']}")
        print("-" * 50)
        
    
    def display_all(self, inventory):
        print("Current Inventory")
        print("-" * 48)
        if not inventory:
            print("Inventory is empty.")
        for items in inventory:
            print(f"ID: {items['id']} | Name: {items['name']} | Price: {items['price']} | Stock: {items['stock']}")
        print("-" * 48)
    

def load_inventory():
    try:
        with open("data/inventory.json", "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        inventory = []
        save_inventory(inventory)  # creates data/inventory.json
        return []

def save_inventory(inventory):
    # items.append([order_id, product_name, quantity])
    with open("data/inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved.")
        # file.write(f"{order_id},{product_name},{quantity},")
        
def menu():
    print("=" * 30)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 30)
    print("-" * 10 + "MENU" + "-" * 10)
    print("""1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit""")
    print("-" * 20)
    inventory = load_inventory()
    
    if not inventory:
        add_product(inventory, "P001", "Laptop", 1200.00, 15)
        add_product(inventory, "P002", "Mouse", 25.50, 40)
        add_product(inventory, "P003", "Keyboard", 45.00, 25)
        
    while True:
        option = input("Enter option: ")
        
        if option == "" or not option.isdigit():
            print("Please input a number")
        elif option == "1":
            self.display_all(inventory)
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            if self.find_product(inventory, product_id):
                print("The selected product already exists")
                continue
            product_name = input("Product Name: ")
            price = input("Price: ")
            stock = input("Stock Quantity: ")
            self.add_product(inventory, product_id, product_name, price, stock)
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            self.search_product(inventory, product_id)
            new_stock = input("New Stock Quantity: ")
            self.update_stock(inventory, product_id, new_stock)
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            self.search_product(inventory, product_id)
        elif option == "5":
            print("Saving inventory...")
            self.save_inventory(inventory)
            print("Inventory saved successfully to data/inventory.json")
        elif option == "6":
            print("Saving inventory before exit...")
            self.save_inventory(inventory)
            print("Inventory saved successfully. \n")
            print("Thank you for using Inventory Management System")
            print("Program terminated.")
            break
        
if __name__ == "__main__":
    Product().menu()
    
    # load_inventory()
    # while True:
    #     delivery = get_valid_input()

    #     if delivery == "quit":
    #         load_inventory()
    #         break
        
    #     inventory = process_delivery(inventory, delivery)

    #     if inventory > 500:
    #         print("Inventory limit exceeded!")
    #         break
        
    #     tax = calculate_tax(delivery)
    #     deliveries_processed += 1
    #     product_name = str(input("Enter Product Name: "))
    #     order_id += 1
    #     save_inventory(order_id,product_name,stock)
    #     print(f"Delivery tax: {tax:.2f}")
    #     print(f"Current inventory: {inventory}")

    # generate_report(deliveries_processed, rejected_entries)