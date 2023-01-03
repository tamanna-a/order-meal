from dataclasses import dataclass

import sqlalchemy as sa
from app import db
from typing import List
from app import create_app

@dataclass
class Kitchen(db.Model):
    '''
    kitchen's children table: Items, Orders
    '''
    __tablename__ = "kitchen"

    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(80), nullable=False)

    items:dict = db.relationship('Item', backref = 'kitchen')
    orders = db.relationship('Order', backref = 'kitchen')


    def __repr__(self):
        return '<User %r>' % self.name

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
    app = create_app()
    with app.app_context():
        kitA = Kitchen(name = 'kitA')
        kitA.save_to_db()

        print(Kitchen.find_id('kitA'))
        print(Kitchen.find_all())

        kitA.delete_from_db()


