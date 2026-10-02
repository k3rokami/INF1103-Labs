import json
import os

FILE = "data.json"


def load_data():
    if not os.path.exists(FILE):
        return {"users": []}
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


# CREATE
def create_user(name, email):
    data = load_data()

    new_id = 1
    for user in data["users"]:
        if user["id"] >= new_id:
            new_id = user["id"] + 1

    new_user = {
        "id": new_id,
        "name": name,
        "email": email
    }
    data["users"].append(new_user)
    save_data(data)
    print("Created user", new_id)


# READ
def read_users():
    data = load_data()
    for user in data["users"]:
        print(user)


def read_user(user_id):
    data = load_data()
    for user in data["users"]:
        if user["id"] == user_id:
            print(user)
            return user
    print("User not found")


# UPDATE
def update_user(user_id, name=None, email=None):
    data = load_data()
    for user in data["users"]:
        if user["id"] == user_id:
            if name is not None:
                user["name"] = name
            if email is not None:
                user["email"] = email
            save_data(data)
            print("Updated user", user_id)
            return
    print("User not found")


# DELETE
def delete_user(user_id):
    data = load_data()

    remaining = []
    for user in data["users"]:
        if user["id"] != user_id:
            remaining.append(user)

    data["users"] = remaining
    save_data(data)
    print("Deleted user", user_id)


# Demo
if __name__ == "__main__":
    create_user("Charlie", "charlie@example.com")
    read_users()
    update_user(1, name="Alice Smith")
    delete_user(2)
    read_users()