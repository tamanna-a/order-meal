from vendor import Vendor
from customer import Customer
from menu import Menu

class Order:
    def __init__(self, vendor, customer):
        self.vendor = vendor
        self.customer = customer
        self.order_id = 1

    def calculate_price(self):
        return 0

    def get_status(self):
        return

    def get_price(self):
        return



if __name__ == '__main__':
    cust = Customer('John')
    print(cust)
    vend = Vendor('Indian')
    print(vend)
    menu = Menu(vend)
    a = menu.add_new_item('rice', 5)
    b = menu.add_new_item('beans', 5)
    print(menu)
    order = Order(cust, vend)

