import json
import os


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Manages its own state
    def update_stock(self, new_stock):
        if new_stock < 0:
            print("Stock cannot be negative. Update cancelled.")
            return False
        self.__stock = new_stock
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")


class Inventory:
    def __init__(self):
        self.__products = []

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product
        return None

    def add_product(self, product):
        if self.search_product(product.get_product_id()):
            return False
        self.__products.append(product)
        return True

    def display_all(self):
        print("Current Inventory")
        print("-" * 48)
        if not self.__products:
            print("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_products(self):
        return self.__products


# ---------- File handling ----------
def load_inventory():
    inventory = Inventory()
    try:
        with open("data/inventory.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return inventory

    if isinstance(data, list):
        for item in data:
            product = Product(item["id"], item["name"],
                              float(item["price"]), int(item["stock"]))
            inventory.add_product(product)
    return inventory


def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })
    os.makedirs("data", exist_ok=True)
    with open("data/inventory.json", "w") as f:
        json.dump(data, f, indent=4)


# ---------- Main program ----------
def show_menu():
    print("=" * 30)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 30)
    print("-" * 10 + "MENU" + "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 20)


def main():
    inventory = load_inventory()

    if not inventory.get_products():
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))

    show_menu()

    while True:
        option = input("Enter option: ")

        if option == "" or not option.isdigit():
            print("Please input a number")
        elif option == "1":
            inventory.display_all()
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            if inventory.search_product(product_id):
                print("The selected product already exists")
                continue
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid price or stock. Product not added.")
                continue
            inventory.add_product(Product(product_id, name, price, stock))
            print("Product added successfully!")
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product is not found.")
                continue
            product.display_information()
            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid quantity.")
                continue
            if product.update_stock(new_stock):
                print("Product stock updated successfully.")
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product is not found.")
            else:
                print("Product Found")
                print("-" * 50)
                product.display_information()
                print("-" * 50)
        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to data/inventory.json")
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully. \n")
            print("Thank you for using Inventory Management System")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()