from item import Item


class Menu:
    """
    Menu class is associated with a vendor. It allows
    adding item and deleting item from menu.
    You can also change price of item
    """
    def __init__(self, vendor_id):
        self.vendor_id = vendor_id
        self.items = []

    def add_new_item(self, name, price):
        item_id = len(self.items)
        item = Item(self.vendor_id, item_id, name, price)
        self.items.append(item)
        return item

    def change_item_price(self, item, new_price):
        item.change_price(new_price)

    def get_all_items(self):
        return self.items

    def delete_item_by_object(self, item):
        self.items.remove(item)

    def delete_item_by_id(self, item_id):
        item = self.get_item_by_id(item_id)
        self.items.remove(item)

    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None


    def __str__(self):
        str = ''
        for item in self.items:
            str+= item.__str__() + ' \n'
        return str



if __name__ == '__main__':
    m = Menu(1)
    r= m.add_new_item('rice', 5)
    b= m.add_new_item('beans', 6)
    print(m)
    #m.delete_item(b)
    #print(m)
    c = m.get_item_by_id(0)
    print('c', c)
    m.delete_item_by_id(0)
    print(m)