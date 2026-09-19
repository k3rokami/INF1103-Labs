def get_valid_age():
    while True:
        age_input = input("Enter your age: ")
        if age_input.isdigit():
            return int(age_input)  # Exits the loop and the function instantly
        print("Invalid input. Please enter numbers only.")

get_valid_age()