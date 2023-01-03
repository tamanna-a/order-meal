from app.pythononly.vendor import Vendor
from app.pythononly.customer import Customer
from app.pythononly.menu import Menu

class Cart:
    def __init__(self, vendor, customer):
        self.vendor = vendor
        self.customer = customer
        self.cart = []
        #dictionary object [{item:_, qty:_, price:_}, {}]

    def add_item_to_cart(self, item):
        return

    def delete_from_cart(self, item):
        return

    def add_qty(self, item):
        return

    def remove_qty(self, item):
        return

    def total_price(self):
        return

    def calculate_price(self):
        return 0


if __name__ == '__main__':
    cust = Customer('John')
    print(cust)
    vend = Vendor('Indian')
    print(vend)
    menu = Menu(vend)
    a = menu.add_new_item('rice', 5)
    b = menu.add_new_item('beans', 5)
    print(menu)
    order = Cart(cust, vend)

