import sqlalchemy as sa
from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from typing import List
#from app.models.order import Order

'''
Import UserMixin
This allows us to use methods such as 
- is_authenticated(), 
- is_active(), 
- is_anonymous(), and 
- get_id ()
'''
class User(db.Model, UserMixin):
    __tablename__ = "user"

    #id will be automatically created, it's primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    orders = db.relationship('Order', backref = "customer")

    def __repr__(self):
        return '<User %r>' % self.username

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