from flask import Blueprint
import json
from flask import Flask, session, render_template, jsonify,request, redirect, url_for, flash
from app import db
from app.models.item import Item
from app.models.kitchen import Kitchen

menu = Blueprint('menu', __name__,template_folder='templates')

@menu.route('/menu', methods=['GET', 'POST'])
def see_menu():
    input = 'mels'
    kitchen = Kitchen.query.filter_by(name = input).first()
    items = kitchen.items

    bean = Item(name='beans', price='10')
    bean = jsonify(bean)
    print(bean)
    #session['items'] = items
    return render_template("menu.html", menus = items)

@menu.route('/get_json')
def get_json():
    # TODO: flask sql alchemy results to json- https://www.reddit.com/r/flask/comments/vll4xu/af_how_to_turn_flask_sqlalchemy_query_results/
    # item = Item.query.filter_by(name='rice').first()
    kitchen = Kitchen.query.filter_by(name = 'mels').first()
    kitchen = json.dumps(kitchen)
    print(type(kitchen))

    print(kitchen.id, kitchen.items)

    return kitchen

@menu.route('/menu-all')
def menu_test():
    """the home page"""
    #menus = Menu.query.order_by(Menu.id)
    #return render_template("menu.html", menus = menus)
    return

