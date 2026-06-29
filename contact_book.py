import json, os

FILE = "contacts.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return {}

def save(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add(contacts):
    name  = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts[name] = {"phone": phone, "email": email}
    save(contacts)
    print(f"Added {name}.")

def view(contacts):
    if not contacts:
        print("No contacts.")
        return
    print(f"\n{'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 55)
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info['email']}")

def delete(contacts):
    name = input("Name to delete: ")
    if name in contacts:
        del contacts[name]
        save(contacts)
        print(f"Deleted {name}.")
    else:
        print("Not found.")

def main():
    contacts = load()
    while True:
        print("\n1. View  2. Add  3. Delete  0. Quit")
        choice = input("Choice: ")
        if choice == "1": view(contacts)
        elif choice == "2": add(contacts)
        elif choice == "3": delete(contacts)
        elif choice == "0": break

main()
