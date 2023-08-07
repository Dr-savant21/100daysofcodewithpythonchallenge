contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone Number: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def show_all_contacts():
    if contacts:
        print("All Contacts:")
        for name, phone_number in contacts.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
    else:
        print("No contacts found.")

# Example usage
add_contact("John", "1234567890")
add_contact("Alice", "9876543210")
add_contact("Bob", "5555555555")

search_contact("Alice")
search_contact("Dave")

delete_contact("John")
delete_contact("Eve")

show_all_contacts()
