import sqlite3

conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")
conn.commit()


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    cursor.execute(
        "INSERT INTO contacts (name, phone) VALUES (?, ?)",
        (name, phone)
    )
    conn.commit()
    print("Contact added successfully.")


def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()

    if not contacts:
        print("No contacts found.")
        return

    print("----- CONTACTS -----")
    for contact in contacts:
        print(f"ID: {contact[0]}")
        print(f"Name: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print("-" * 20)


def update_contact():
    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()

    if not contact:
        print("Contact not found.")
        return

    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone number: ")

    cursor.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?", (new_name, new_phone, contact_id))

    conn.commit()
    print("Contact updated successfully.")


def delete_contact():
    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = cursor.fetchone()

    if not contact:
        print("Contact not found.")
        return

    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()

    print("Contact deleted successfully.")

def sort_contacts():
    cursor.execute("""SELECT * FROM contacts 
                    ORDER BY name ASC""")

    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"ID: {contact[0]}")
        print(f"Name: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print("-" * 20)

while True:
    print("===== PHONE BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Sort Contacts")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        sort_contacts()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

conn.close()