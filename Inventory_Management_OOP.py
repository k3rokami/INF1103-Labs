from Product import Product
from Inventory import Inventory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
import json

def load_inventory(inventory):
    try:
        with open("data/inventory.json", "r") as file:
            product_data = json.load(file)
        for item in product_data:
            supplier_data = item.get("supplier")
            if supplier_data is None:
                supplier = Supplier("UNKNOWN", "Unknown Supplier", "")
            else:
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["weight"],
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    supplier
                )
            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["download_size"],
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    supplier
                )
            else:
                print(f"Unknown product type: {item['type']}")
                continue
            inventory.add_product(product)

    except FileNotFoundError:
        print("No saved inventory found.")
    
def product_to_dict(product):
    product_data = {
        "product_id": product.get_product_id(),
        "name": product.get_name(),
        "price": product.get_price(),
        "stock": product.get_stock(),
        "supplier": {
            "supplier_id": product.supplier.get_supplier_id(),
            "name": product.supplier.get_name(),
            "contact_email": product.supplier.get_contact_email()
        }
    }
    if isinstance(product, PhysicalProduct):
        product_data["type"] = "physical"
        product_data["weight"] = product.get_weight()

    elif isinstance(product, DigitalProduct):
        product_data["type"] = "digital"
        product_data["download_size"] = product.get_download_size()

    return product_data

def save_inventory(products):
    product_data = []

    for product in products:
        product_data.append(product_to_dict(product))

    with open("data/inventory.json", "w") as file:
        json.dump(product_data, file, indent=4)
    
def menu():
    # inventory = load_inventory()
    inventory = Inventory()
    load_inventory(inventory)

    if not inventory.get_products():
        supplier = Supplier("S001", "Razer Inc", "Razer@razer.com")
        product = PhysicalProduct(2.5, "P001", "Laptop", 1200.00, 15, supplier)
        inventory.add_product(product)
        product = PhysicalProduct(0.5, "P002", "Mouse", 25.50, 40, supplier)
        inventory.add_product(product)
        product = PhysicalProduct(1.3, "P003", "Keyboard", 45.00, 25, supplier)
        inventory.add_product(product)
        
    while True:
        print("\n===== Inventory Management System =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        option = input("Enter your choice: ")
        
        if option == "" or not option.isdigit():
            print("Please input a number")
            
        elif option == "1":
            inventory.display_all()
            
        elif option == "2":
            print("Add New Product")
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock: "))
            supplier_id = input("Enter Supplier ID: ")
            supplier_name = input("Enter Supplier Name: ")
            supplier_email = input("Enter Supplier Email: ")
            supplier = Supplier(supplier_id, supplier_name, supplier_email)
            while True:
                product_info = input("Is the product Digital or Physical? (D/P): ").strip()
                if product_info == "D":
                    download_size = float(input("Enter download size (MB): "))
                    product = DigitalProduct(download_size, product_id, name, price, stock, supplier)
                    print(product.get_fulfillment_info())
                    break
                elif product_info == "P":
                    weight = float(input("Enter weight (kg): "))
                    product = PhysicalProduct(weight, product_id, name, price, stock, supplier)
                    print(product.get_fulfillment_info())
                    break
                else:
                    print("Invalid Option! Select either D or P.")
            inventory.add_product(product)
            print("Product added successfully!")
            
        elif option == "3":
            print("Update Stock")
            product_id = input("Enter Product ID: ")
            new_stock = int(input("Enter new stock quantity: "))
            inventory.update_stock(product_id, new_stock)
            
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)
            if product is None:
                print("Product not found.")
            else:
                product.display_information()
                
        elif option == "5":
            print("Saving inventory...")
            products = inventory.get_products()
            save_inventory(products)
            print("Inventory saved successfully to data/inventory.json")
            
        elif option == "6":
            print("Saving inventory before exit...")
            products = inventory.get_products()
            save_inventory(products)
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