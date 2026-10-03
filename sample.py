import json

FILE = "inventory.json"


# ---------- Persistence ----------
def load_inventory():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
        print("inventory.json found. Inventory loaded successfully.")
        return data if isinstance(data, list) else []
    except FileNotFoundError:
        print("inventory.json not found. Creating a new inventory.")
        save_inventory([])
        return []


def save_inventory(inventory):
    with open(FILE, "w") as f:
        json.dump(inventory, f, indent=4)


# ---------- Functions ----------
def find_product(inventory, product_id):
    for product in inventory:
        if product["id"].lower() == product_id.lower():
            return product
    return None


def add_product(inventory, product_id, name, price, stock):
    if find_product(inventory, product_id):
        print("Product ID already exists.")
        return
    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("Product added successfully!")


def update_stock(inventory, product_id, new_stock):
    product = find_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    product["stock"] = new_stock
    print("Stock updated successfully!")


def search_product(inventory, product_id):
    product = find_product(inventory, product_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)


def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    if not inventory:
        print("Inventory is empty.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | "
              f"Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


# ---------- Menu ----------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    # Make sure there are at least three products
    if not inventory:
        add_product(inventory, "P001", "Laptop", 1200.00, 15)
        add_product(inventory, "P002", "Mouse", 25.50, 40)
        add_product(inventory, "P003", "Keyboard", 45.00, 25)

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            print("Add New Product")
            product_id = input("Product ID: ").strip()
            name = input("Product Name: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Invalid number. Product not added.")
                continue
            add_product(inventory, product_id, name, price, stock)

        elif choice == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ").strip()
            product = find_product(inventory, product_id)
            if product is None:
                print("Product not found.")
                continue
            print(f"Product Found: Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Invalid number. Stock not changed.")
                continue
            update_stock(inventory, product_id, new_stock)

        elif choice == "4":
            print("Search Product")
            search_product(inventory, input("Enter Product ID: ").strip())

        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please choose 1-6.")


main()