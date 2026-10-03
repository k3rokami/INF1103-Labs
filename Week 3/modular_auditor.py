inventory = 0
deliveries_processed = 0
rejected_entries = 0

def get_valid_input():
    global rejected_entries
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


while True:
    delivery = get_valid_input()

    if delivery == "quit":
        break
    
    inventory = process_delivery(inventory, delivery)
    
    if inventory > 500:
        print("Inventory limit exceeded!")
        break
    
    tax = calculate_tax(delivery)
    deliveries_processed += 1
    print(f"Delivery tax: {tax:.2f}")
    print(f"Current inventory: {inventory}")

generate_report(deliveries_processed, rejected_entries)