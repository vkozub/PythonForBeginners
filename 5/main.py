"""Module Main"""

from contact import Contact
from contact_list import ContactList

contact_list = ContactList()

while True:
    try:
        name = input('name: ')
        email = input('email: ')
        age = input('age: ')
        new_contact = Contact(name, email, age)
        contact_list.add_to_contact_list(new_contact)
    except ValueError as e:
        print(e)
        continue

    proceed = input('add another one? (y/n): ')

    if proceed != 'y':
        break

print(contact_list)
