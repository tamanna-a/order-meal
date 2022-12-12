
class Item:
    def __init__(self, vendor_id, item_id, name,  price):
        self.vendor_id = vendor_id
        self.name = name
        self.price = price
        self.item_id = item_id

    def change_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f'id: {self.item_id}, item: {self.name}, price: {self.price}'




