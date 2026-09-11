Inventory = 0
Rejected = 0

while True:
    Stock = input("Enter the stock item (type 'quit' to exit): ")
    if Stock.lower() == 'quit':
        break

    if Stock.isdigit():
        stock_value = int(Stock)
    else:
        print("Invalid input. Please enter a valid number.")
        Rejected += 1
        print(f"Rejected entries: {Rejected}")
        continue

    if stock_value < 0:
        print("Invalid input. Please enter a non-negative number.")
        Rejected += 1
        print(f"Rejected entries: {Rejected}")
        continue

    Inventory += stock_value
    print(f"Current inventory: {Inventory}")

    if Inventory > 500:
        print("Inventory limit exceeded!")
        break

print(f"Current inventory: {Inventory}")
print(f"Rejected entries: {Rejected}")