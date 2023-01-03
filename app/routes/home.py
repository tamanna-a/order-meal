from flask import Blueprint
import json
from flask import Flask, session, render_template, request, redirect, url_for, flash
from app import db
from app.models.user import User
from app.models.kitchen import Kitchen
from app.models.item import Item
from app.models.order import Order
from app.models.item_in_order import ItemInOrder

home = Blueprint('home', __name__,template_folder='templates')

@home.route('/')
def home_page():
    """the home page"""
    return render_template('home.html')
    #return 'hello'

@home.route('/test')
def test():
    db.drop_all()
    db.create_all()
    print('initialized db')

    # create user
    #bob = User('bob', 'bob@gmail.com', 'bobbob')
    #bob.save_to_db()

    # create Kitchen
    melskitchen = Kitchen(name = 'mels')
    melskitchen.save_to_db()

    # create item
    rice = Item(name = 'rice', price = '5', kitchen = melskitchen)
    rice.save_to_db()

    # add item to kitchen as a list
    beans = Item(name = 'beans', price = '10')
    melskitchen.items.append(beans)
    melskitchen.save_to_db()

    #create order
    o1 = Order(kitchen = melskitchen)
    o1.save_to_db()
    o2 = Order()
    melskitchen.orders.append(o2)
    melskitchen.save_to_db()

    #add items to order
    o3 = Order(kitchen = melskitchen)
    i1 = ItemInOrder(item = beans , quantity = 2)
    o3.items.append(i1)
    #o3.items.extend([rice, beans])
    o3.save_to_db()

    return 'hello'



#background process happening without any refreshing
@home.route('/ajax')
def ajax():
    # TODO: add increment button on javascript- https://www.youtube.com/watch?v=hqGUMqpuFKk&ab_channel=Indently

    #when user clicks on button, it sends GET request
    #text = request.args.get('button_text')
    #print('button text: ', text)
    return render_template('increment.html')

    
