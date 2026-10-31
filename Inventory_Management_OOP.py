import json
from pathlib import Path


INVENTORY_FILE = Path(__file__).parent / "data" / "inventory.json"


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def matches_id(self, product_id):
        return self.__product_id.casefold() == product_id.casefold()

    @property
    def product_id(self):
        return self.__product_id

    def update_stock(self, new_stock):
        self.__stock = new_stock

    def display(self):
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price}")
        print(f"Stock: {self.__stock}")

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }


class Inventory:
    def __init__(self, products=None):
        # Inventory owns Product objects; menu and file code use its methods.
        self.__products = list(products) if products is not None else []

    def is_empty(self):
        return not self.__products

    def find_product(self, product_id):
        for product in self.__products:
            if product.matches_id(product_id):
                return product
        return None

    def add_product(self, product):
        if self.find_product(product.product_id):
            return False
        self.__products.append(product)
        return True

    def update_stock(self, product_id, new_stock):
        product = self.find_product(product_id)
        if product is None:
            print("Product is not found.")
            return False
        product.update_stock(new_stock)
        print("Product stock updated successfully.")
        return True

    def search_product(self, product_id):
        product = self.find_product(product_id)
        if product is None:
            print("Product is not found.")
            return
        print("Product Found")
        print("-" * 50)
        product.display()
        print("-" * 50)

    def display_all(self):
        print("Current Inventory")
        print("-" * 48)
        if self.is_empty():
            print("Inventory is empty.")
        for product in self.__products:
            product.display()
        print("-" * 48)

    def to_list(self):
        return [product.to_dict() for product in self.__products]


def load_inventory():
    try:
        with INVENTORY_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        inventory = Inventory()
        save_inventory(inventory)
        return inventory

    if not isinstance(data, list):
        raise ValueError("Inventory JSON must contain a list of products.")

    # JSON stores dictionaries; convert them to Product objects at the file boundary.
    products = [
        Product(
            item["id"],
            item["name"],
            float(item["price"]),
            int(item["stock"]),
        )
        for item in data
    ]
    return Inventory(products)


def save_inventory(inventory):
    INVENTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with INVENTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(inventory.to_list(), file, indent=4)
    print("Inventory saved.")


def read_required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def read_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Enter a non-negative whole number.")


def read_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
        except ValueError:
            pass
        print("Enter a non-negative price.")


def menu():
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
    inventory = load_inventory()

    if inventory.is_empty():
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))

    while True:
        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()
        elif option == "2":
            print("Add New Product")
            product_id = read_required_text("Product ID: ")
            if inventory.find_product(product_id):
                print("The selected product already exists.")
                continue
            product_name = read_required_text("Product Name: ")
            price = read_non_negative_float("Price: ")
            stock = read_non_negative_int("Stock Quantity: ")
            inventory.add_product(Product(product_id, product_name, price, stock))
            print("Product added successfully!")
        elif option == "3":
            print("Update Stock")
            product_id = read_required_text("Enter Product ID: ")
            if inventory.find_product(product_id) is None:
                print("Product is not found.")
                continue
            new_stock = read_non_negative_int("New Stock Quantity: ")
            inventory.update_stock(product_id, new_stock)
        elif option == "4":
            product_id = read_required_text("Enter Product ID: ")
            inventory.search_product(product_id)
        elif option == "5":
            save_inventory(inventory)
        elif option == "6":
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Please enter an option from 1 to 6.")


if __name__ == "__main__":
    menu()
