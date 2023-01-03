from user import User

class Vendor(User):
    def __init__(self, name,email = None, phone = None,
                 desc = None,
                 addr = None,
                 photo = None):
        super().__init__(name, email, phone, addr)

        self.description = desc
        self.photo = photo

    def __str__(self):
        return self.name

    def add_or_change_description(self, desc):
        self.description= desc

    def add_or_change_photo(self, photo):
        self.photo = photo



if __name__ == '__main__':
    v = Vendor('indian')
    print(v)
    v.add_or_change_description('i prepare home cooked meals')
    print(v.description)
    print(v.address)