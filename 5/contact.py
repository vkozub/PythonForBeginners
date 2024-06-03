"""Module Contact class."""

class Contact:
    """Contact class."""

    def __init__(self, name, email, age):
        self.name = self.validate_name(name)
        self.email = self.validate_email(email)
        self.age = self.validate_age(age)

    @staticmethod
    def validate_name(name):
        """Validate name."""
        if len(name) > 50:
            raise ValueError('Name is too large!')
        return name

    @staticmethod
    def validate_email(email):
        """Validate email."""
        if '@' not in email or '.' not in email:
            raise ValueError('Invalid email!')
        return email

    @staticmethod
    def validate_age(age):
        """Validate age."""
        age = int(age)  # Python will raise ValueError if not numeric
        if age <= 0:
            # We ask Python to raise ValueError if <= 0
            raise ValueError('Invalid age!')
        return age

    def __str__(self) -> str:
        return f'Full name: {self.name}, age: {self.age}, email: {self.email}'
