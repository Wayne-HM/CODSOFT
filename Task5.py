#Task 5-Contact Book
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if results:
            for contact in results:
                self.display_contact(contact)
        else:
            print("No contacts found.")

    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print("Contact found:")
                self.display_contact(contact)
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone to search: ")
            contact_book.search_contact(query)
        elif choice == '4':
            query = input("Enter name or phone to update: ")
            contact_book.update_contact(query)
        elif choice == '5':
            query = input("Enter name or phone to delete: ")
            contact_book.delete_contact(query)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
