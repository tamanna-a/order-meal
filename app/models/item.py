from dataclasses import dataclass

import sqlalchemy as sa
from app import db
from typing import List
from app.models.kitchen import Kitchen
import json

@dataclass
class Item(db.Model):
    '''
    Many to one with kitchen
    Many to one with orderItems
    '''
    __tablename__ = "item"

    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)

    kitchen_id = db.Column(db.Integer, db.ForeignKey('kitchen.id'),nullable=False)

    items = db.relationship("ItemInOrder", backref = 'item')


    def __repr__(self):
        return '<User %r>' % self.name

    def toJSON(self):
        return json.dumps(self.__dict__)

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

if __name__ == '__main__':
    kitA = Kitchen(name = 'kitA')

    db.session.add(kitA)
    db.session.commit()


