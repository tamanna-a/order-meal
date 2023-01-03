import sqlalchemy as sa
from app import db
from typing import List


class ItemInCart(db.Model):
    '''
    Join table that maintains relationship between order and items
    One to one relationship with order
    one to one relationship with items
    '''
    __tablename__ = "item_in_cart"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column("item_id", db.Integer, db.ForeignKey("item.id"))
    cart_id = db.Column("cart_id", db.Integer, db.ForeignKey("cart.id"))

    quantity = db.Column(db.Integer)

