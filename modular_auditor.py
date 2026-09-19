Inventory = 0
Rejected = 0

def get_valid_input():
    while True:
        user_input = input("Enter the stock item (type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            return None
        elif not user_input.isdigit() or int(user_input) < 0:
            global Rejected
            print("Invalid input. Please enter a valid number.")
            Rejected += 1
            print(f"Rejected entries: {Rejected}")
        else:
            global Inventory
            Inventory += int(user_input)
            return Inventory

# def process_delivery(current_total, new_value):


# def caculate_tax(amount):
#     return amount * 0.10

# def generate_report(total_unit,failed_atempts):

    

while True:
    get_valid_input()
    print(Inventory)
    # Stock = input("Enter the stock item (type 'quit' to exit): ")
        
    # if Stock.lower() == 'quit':
    #     break
    
    # if not Stock.isdigit() or int(Stock) < 0:
    #     print("Invalid input. Please enter a valid number.")
    #     Rejected += 1
    #     print(f"Rejected entries: {Rejected}")
    # else:
    #     Inventory += int(Stock)
        
    # print(f"Current inventory: {Inventory}")
    
    # if Inventory > 500:
    #     print("Inventory limit exceeded!")
    #     break
    
# print(f"Current inventory: {Inventory}")
# print(f"Rejected entries: {Rejected}")