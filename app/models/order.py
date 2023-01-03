import sqlalchemy as sa
from app import db
from typing import List
from flask_login import UserMixin


class Order(db.Model, UserMixin):
    '''
    Many to one relationship with kitchen
    One to one with OrderItems
    '''
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)

    kitchen_id = db.Column(db.Integer, db.ForeignKey('kitchen.id'),nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    #Order.items -> ItemInOrder
    # ItemInOrder.order -> Order.items
    items = db.relationship("ItemInOrder",
                            backref = 'order') #OrderItem.orders


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




