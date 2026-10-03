import json

# inventory = 0
# deliveries_processed = 0
# rejected_entries = 0
# order_id = 1000
# items = []

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


def find_product(inventory, product_id):
    for product in inventory:
        if product['id'].lower() == product_id.lower():
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
    if product == None:
        print("Product is not found.")
        return
    product['stock'] = new_stock
    print("Product stock updated successfully.")
        
def search_product(inventory, product_id):
    product=find_product(inventory, product_id)
    if product == None:
        print("Product is not found.")
        return
    print("Product Found")
    print("-" * 50)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 50)
    
def display_all(inventory):
    print("Current Inventory")
    print("-" * 48)
    if not inventory:
        print("Inventory is empty.")
    for items in inventory:
        print(f"ID: {items['id']} | Name: {items['name']} | Price: {items['price']:.2f} | Stock: {items['stock']}")
    print("-" * 48)

# def old_load_inventory():
#     global items, order_id
#     print("Current Orders:")
#     try:
#         with open("inventory.txt", "r") as file:
#             for line in file:
#                 line = line.strip()
#                 if not line:
#                     continue
#                 parts = [p.strip() for p in line.split(",") if p.strip() != ""]
#                 for i in range(0, len(parts), 3):
#                     if i + 2 >= len(parts):
#                         break
#                     order_id = int(parts[i])
#                     name = parts[i + 1]
#                     qty = int(parts[i + 2])
#                     items.append([order_id, name, qty])
#                     print(f"{order_id}, {name}, {qty}")
#                     order_id += qty
#     except FileNotFoundError:
#         with open("inventory.txt", "w") as file:
#             pass
        

# def get_valid_input():
#     global rejected_entries,stock
#     while True:
#         stock = input("Enter the stock quantity (type 'quit' to exit): ").strip()

#         if stock.lower() == "quit":
#             return "quit"
        
#         if not stock.isdigit() or int(stock) < 0:
#                 print("Invalid input. Please enter a non-negative whole number.")
#                 rejected_entries += 1
                
#         else:
#             return int(stock)
                
        # try:
        #     value = int(stock)
        #     if value < 0:
        #         raise ValueError
        #     return value
        # except ValueError:
        #     audit_state["failed_attempts"] += 1
        #     print("Invalid input. Please enter a non-negative whole number.")
    
# def process_delivery(current_total, new_value):
#     return current_total + new_value


# def calculate_tax(amount):
#     return amount * 0.10


# def generate_report(total_units, failed_attempts):
#     print(f"Total Deliveries Processed: {total_units}")
#     print(f"Number of Failed/Rejected Entries: {failed_attempts}")

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
            display_all(inventory)
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ")
            if find_product(inventory, product_id):
                print("The selected product already exists")
                continue
            product_name = input("Product Name: ")
            price = input("Price: ")
            stock = input("Stock Quantity: ")
            add_product(inventory, product_id, product_name, price, stock)
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            search_product(inventory, product_id)
            new_stock = input("New Stock Quantity: ")
            update_stock(inventory, product_id, new_stock)
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            search_product(inventory, product_id)
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
        
if __name__ == "__main__":
    menu()
    
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