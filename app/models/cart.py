import sqlalchemy as sa
from app import db
from typing import List
from flask_login import UserMixin


class Cart(db.Model, UserMixin):
    '''
    Many to one relationship with kitchen
    One to one with OrderItems
    '''
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)

    kitchen_id = db.Column(db.Integer, db.ForeignKey('kitchen.id'),nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    items = db.relationship("CartInOrder",
                            backref = 'cart')



    def __repr__(self):
        return '<Order %r>' % self.name

    @classmethod
    def find_by_name(cls, name: str):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List:
        return cls.query.all()

    @classmethod
    def find_id(cls, name: str):
        obj = cls.query.filter_by(name=name).first()
        return obj.id

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()



class Product(db.Model):
    #id will be automatically created, it's primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)
    qty = db.Column(db.Integer)

    def __init__(self,  name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {"name": self.name,
                "price": self.price,
                "qty": self.qty}