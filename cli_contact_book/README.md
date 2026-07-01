# 📒 CLI Contact Book

A simple command-line contact book built in Python that stores and retrieves contacts using a JSON file. Built as part of the PaceWisdom Python training program.

---

## 📌 Features

- Add new contacts (name, phone, email)
- View all contacts in a formatted table
- Search for a contact by name
- Update existing contact details
- Delete a contact
- Contacts are saved to a `contacts.json` file — data persists between runs

---

## 🛠️ Tech Stack

- Python 3
- `json` module — for saving/loading contacts
- `os` module — for file existence check
- Dictionaries & Functions

---

## 🚀 How to Run

```bash
python contact_book.py
```

---

## 🖥️ Sample Output

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Choose an option: 1
Name: Vamshika
Phone: 9876543210
Email: vamshika@email.com
Added Vamshika.

Choose an option: 2
Name                Phone          Email                    
------------------------------------------------------------
Vamshika            9876543210     vamshika@email.com       

Choose an option: 3
Enter name to search: Vamshika
Name: Vamshika
Phone: 9876543210
Email: vamshika@email.com

Choose an option: 4
Enter name to update: Vamshika
New phone (9876543210): 9999999999
New email (vamshika@email.com): 
Updated.

Choose an option: 5
Enter name to delete: Vamshika
Deleted.

Choose an option: 6
Goodbye!
```

---

## 📁 File Structure

```
cli_contact_book/
│
├── contact_book.py   # Main Python script
├── contacts.json     # Auto-generated file to store contacts
└── README.md         # Project documentation
```

---

## 👩‍💻 Author

**Vamshika** — [github.com/vamshikavw](https://github.com/vamshikavw)
