
class User:
    def __init__(self, name,
                 email = None,
                 phone = None,
                 addr = None):

        self.name = name
        self.email = email
        self.phone = phone
        self.address = addr


    def __str__(self):
        return self.name

    def add_or_change_email(self, email):
        self.email = email

    def add_or_change_phone(self, phone):
        self.phone = phone

    def add_or_change_address(self, addr):
        self.address = addr


if __name__ == '__main__':
    v = User('Tom', 'abc@gmail.com', '916-586-9269')
    print(v)
    print(v.email)
    print(v.phone)
