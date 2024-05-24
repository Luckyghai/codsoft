# Define a Contact class to store information
class Contact:
  def __init__(self, name, phone_number, email, address):
    self.name = name
    self.phone_number = phone_number
    self.email = email
    self.address = address

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Phone Number: {self.phone_number}")
    print(f"Email: {self.email}")
    print(f"Address: {self.address}")

# Create an empty list to store contacts
contacts = []

def main_menu():
  print("\nContact Book")
  print("1. Add Contact")
  print("2. View All Contacts")
  print("3. Search Contact")
  print("4. Exit")
  choice = input("Enter your choice: ")
  return choice

def add_contact():
  name = input("Enter name: ")
  phone_number = input("Enter phone number: ")
  email = input("Enter email address (optional): ")
  address = input("Enter address (optional): ")
  contact = Contact(name, phone_number, email, address)
  contacts.append(contact)
  print("Contact added successfully!")

def view_contacts():
  if not contacts:
    print("There are no contacts in the book.")
    return
  for contact in contacts:
    contact.display_info()
    print("-" * 20)

def search_contact():
  name = input("Enter name to search: ")
  found = False
  for contact in contacts:
    if contact.name.lower() == name.lower():
      contact.display_info()
      found = True
  if not found:
    print(f"Contact '{name}' not found.")

while True:
  choice = main_menu()
  if choice == '1':
    add_contact()
  elif choice == '2':
    view_contacts()
  elif choice == '3':
    search_contact()
  elif choice == '4':
    print("Exiting Contact Book...")
    break
  else:
    print("Invalid choice. Please try again.")
