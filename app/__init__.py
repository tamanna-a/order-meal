from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import timedelta
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

import click
from flask.cli import with_appcontext




#create database object
db = SQLAlchemy()

class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)

@click.command(name = 'create')
@with_appcontext #puts app context like db configuration
def create():
    db.create_all()

#create app
def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = uuid.uuid4().hex
    # Intialize MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #store permanent session data for 1 data
    app.permanent_session_lifetime = timedelta(days = 1)

    #import blueprints
    from app.routes.home import home
    from app.routes.profile import profile
    from app.routes.auth import auth
    from app.routes.cart import cart
    from app.routes.menu import menu

    #register blueprints
    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(profile)
    app.register_blueprint(cart)
    app.register_blueprint(menu)

    ## create table schema
    # if model defined in other module, import before create
    from app.models.user import User
    from app.models.kitchen import Kitchen
    from app.models.order import Order
    from app.models.item_in_order import ItemInOrder
    from app.models.item import Item


    #create all tables
    with app.app_context():
        db.create_all()

    '''with app.app_context():
        db.create_all()

        # add menu items initially
        # TODO: Add image of menu item here & link it in menu.html
        new_menu = Menu(name='rice', price='7')
        db.session.add(new_menu)
        db.session.commit()
    '''
    app.cli.add_command(create)
    # TODO: add cli command to initdb- https://www.youtube.com/watch?v=4gRMV-wZTQs&ab_channel=darkyodeler

    #set up login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.session_protection = "strong"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app



