from flask import Blueprint, jsonify
import json
from flask import Flask, session, render_template, request, redirect, url_for, flash
from app import db
from app.models.cart import Product
from app.models.kitchen import Kitchen
from app.models.item import Item
from app.models.order import Order
from app.models.item_in_order import ItemInOrder


order = Blueprint('order', __name__,template_folder='templates')

@order.route('/cart', methods = ["GET", "POST"])
def display_order():
    #see all items in cart
    o3 = Order(kitchen = melskitchen, status = 'inCart')

    i1 = ItemInOrder(item = beans , quantity = 2)
    o3.items.append(i1)
    #o3.items.extend([rice, beans])
    o3.save_to_db()

    return



@order.route('/order-deprecated', methods = ["GET", "POST"])
def display_order_deprecated():
    # TODO: add user authentication to cart, in cart.html & cart db
    # TODO: get items from cart
    currentCart = []

    p1 = Product('rice', 5, 6)
    p2 = Product('beans', 7, 8)
    currentCart.append(p1)
    currentCart.append(p2)
    #cart_json = json.dumps(currentCart)
    session['cart'] = p1.serialize()

    # if get request, display cart items
    if request.method == "GET":
        return render_template('cart.html', currentCart=currentCart)

    #else handle submitted cart info
    else:
        # get info from cart
        checkoutCart = session.get('cart')
        # create order
        # TODO: Create order class & submit order
        print(checkoutCart)

        #submit transaction

        #send success note
        return render_template('successOrder.html')


@order.route('/checkout')
def checkout_order():
    checkoutorder = session.get('order')
    print(checkoutorder)
    return render_template('order.html', currentorder = checkoutorder)

@order.route('/order-deprecated', methods=['GET', 'POST'])
def add_to_order():
    # TODO: handle order.1) set up order form 2) submit/place order 3) see orders
    #  2) sending add to cart should send information to cart page
    #  options: 1) server side session with cart object 2)database 3)javascript
    # session- con- gets deleted if user disconnects
    # use local storage- https://www.reddit.com/r/flask/comments/6slfiz/af_creating_an_online_shop_application_whats_the/

    cart = session["cart"]

    if request.method == 'POST':
        if 'cart' not in session:
            session["cart"] = {}

        cart = session["cart"]
        #add items to cart
        itemname = request.form.get("itemname")
        qty = request.form.get("qty")

        #if already in cart, update qty value
        if itemname in cart:
            cart[itemname]

        #otherwise add to cart
        session['cart'].append({'id': itemname, 'quantity':qty})
        session.modified = True

        flash('yay!')

        # if GET
        return render_template('register_vendor.html')

