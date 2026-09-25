inventory = 0
deliveries_processed = 0
rejected_entries = 0
order_id = 1000
items = []

def load_inventory():
    global items, order_id
    print("Current Orders:")
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",") if p.strip() != ""]
                for i in range(0, len(parts), 3):
                    if i + 2 >= len(parts):
                        break
                    order_id = int(parts[i])
                    name = parts[i + 1]
                    qty = int(parts[i + 2])
                    items.append([order_id, name, qty])
                    print(f"{order_id}, {name}, {qty}")
                    order_id += qty
    except FileNotFoundError:
        with open("inventory.txt", "w") as file:
            pass
        
def save_inventory(order_id, product_name, quantity):
    items.append([order_id, product_name, quantity])
    with open("inventory.txt", "a") as file:
        file.write(f"{order_id},{product_name},{quantity},")

def get_valid_input():
    global rejected_entries,stock
    while True:
        stock = input("Enter the stock quantity (type 'quit' to exit): ").strip()

        if stock.lower() == "quit":
            return "quit"
        
        if not stock.isdigit() or int(stock) < 0:
                print("Invalid input. Please enter a non-negative whole number.")
                rejected_entries += 1
                
        else:
            return int(stock)
                
        # try:
        #     value = int(stock)
        #     if value < 0:
        #         raise ValueError
        #     return value
        # except ValueError:
        #     audit_state["failed_attempts"] += 1
        #     print("Invalid input. Please enter a non-negative whole number.")


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


if __name__ == "__main__":
    load_inventory()
    while True:
        delivery = get_valid_input()

        if delivery == "quit":
            load_inventory()
            break
        
        inventory = process_delivery(inventory, delivery)

        if inventory > 500:
            print("Inventory limit exceeded!")
            break
        
        tax = calculate_tax(delivery)
        deliveries_processed += 1
        product_name = str(input("Enter Product Name: "))
        order_id += 1
        save_inventory(order_id,product_name,stock)
        print(f"Delivery tax: {tax:.2f}")
        print(f"Current inventory: {inventory}")

    generate_report(deliveries_processed, rejected_entries)