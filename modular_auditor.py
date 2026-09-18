Inventory = 0
Rejected = 0

def get_valid_input(input_prompt):
    while True:
        user_input = input(input_prompt)
        if user_input.lower() == 'quit':
            return None
        elif not user_input.isdigit() or int(user_input) < 0:
            print("Invalid input. Please enter a valid number.")
            global Rejected
            Rejected += 1
            print(f"Rejected entries: {Rejected}")
        else:
            return int(user_input)

def process_delivery(current_total, new_value):


def caculate_tax(amount):
    return amount * 0.10

def generate_report(total_unity,failed_atempts):


while True:
    Stock = input("Enter the stock item (type 'quit' to exit): ")
        
    if Stock.lower() == 'quit':
        break
    
    if not Stock.isdigit() or int(Stock) < 0:
        print("Invalid input. Please enter a valid number.")
        Rejected += 1
        print(f"Rejected entries: {Rejected}")
    else:
        Inventory += int(Stock)
        
    print(f"Current inventory: {Inventory}")
    
    if Inventory > 500:
        print("Inventory limit exceeded!")
        break
    
print(f"Current inventory: {Inventory}")
print(f"Rejected entries: {Rejected}")