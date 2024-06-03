"""Module Contact List class."""

from contact import Contact

class ContactList:
    """Contact List class."""

    def __init__(self):
        self.storage = []

    def __str__(self) -> str:
        array = []
        for contact in self:
            array.append(contact.__str__())
        array.append(f'Amount of contacts: {len(self)}')
        return '\n'.join(array)

    def __iter__(self):
        return iter(self.storage)

    def __getitem__(self, index):
        return self.storage[index]

    def __len__(self):
        return len(self.storage)

    def add_to_contact_list(self, contact):
        """Adding to list of contact"""
        if not isinstance(contact, Contact):
            raise ValueError('Invalid contact!')
        self.storage.append(contact)
