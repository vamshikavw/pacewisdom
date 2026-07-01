import json
import os

FILE = "contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Added {name}.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print(f"{'Name':<20}{'Phone':<15}{'Email':<25}")
    print("-" * 60)
    for name, info in contacts.items():
        print(f"{name:<20}{info['phone']:<15}{info['email']:<25}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input(f"New phone ({contacts[name]['phone']}): ").strip()
        email = input(f"New email ({contacts[name]['email']}): ").strip()
        contacts[name]["phone"] = phone or contacts[name]["phone"]
        contacts[name]["email"] = email or contacts[name]["email"]
        save_contacts(contacts)
        print("Updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    menu = """
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()