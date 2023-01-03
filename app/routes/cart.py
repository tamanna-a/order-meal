from flask import Blueprint, jsonify
import json
from flask import Flask, session, render_template, request, redirect, url_for, flash
from app import db
from app.models.cart import Product
from app.models.kitchen import Kitchen
from app.models.item import Item
from app.models.order import Order
from app.models.item_in_order import ItemInOrder
from app.models.user import User
from app.models.cart import Cart


cart = Blueprint('cart', __name__,template_folder='templates')

@cart.route('/fillcart')
def fill_cart():
    # see all items in cart
    o3 = Order(kitchen=melskitchen, status='inCart')

    i1 = ItemInOrder(item=beans, quantity=2)
    o3.items.append(i1)
    # o3.items.extend([rice, beans])
    o3.save_to_db()
    return

@cart.route('/cart', methods = ["GET", "POST"])
def display_order():
    if "user" in session:
        #get User
        found_user =  User.query.filter_by(username = session['user']).first()
        cartitems = Cart.query.filter_by(customer_id = found_user.id).first()


    return
