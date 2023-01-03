from app.pythononly.user import User

class Customer(User):
    def __init__(self, name,email = None, phone = None,
                 desc = None,
                 addr = None,
                 photo = None):
        super().__init__(name, email, phone,addr)

        self.photo = photo

    def __str__(self):
        return self.name



if __name__ == '__main__':
    v = Customer('joe')
    print(v)
    print(v.name)
    print(v.email)
    print(v.description)