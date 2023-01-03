from flask import Blueprint
import json
from flask import Flask, session, render_template, request, redirect, url_for, flash
from app import db
from app.models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__,template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Check if Post request & get user info
    if request.method == 'POST':
        # set session to be permanent
        session.permanent = True

        # collect input info
        username = request.form.get('username')
        session["user"] = username
        password = request.form.get('password')
        print(User.query.all())
        # check if user exists
        # queries Users table and returns User object if found
        found_user =  User.query.filter_by(username = username).first()
        if found_user:
            #check password
            if check_password_hash(found_user.password, password):
                flash("Logged in!", category='success')
                login_user(found_user, remember=True)
                return redirect(url_for('home.home_page'))
            else: #password incorrect
                flash('Password is incorrect.', category='error')
        else:#user does not exist
            flash('Email does not exist.', category='error')
            #render login.html

    else:
        # if already logged in
        if "user" in session:
            return redirect(url_for('home.home_page'))

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@auth.route('/register_vendor', methods=['GET', 'POST'])
def register_vendor():
    # if POST
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email = request.form.get("email")
        flash('yay!')

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 3:
            flash('Password is too short.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(
                password1, method='sha256'), email=email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('home.home_page'))

    # if GET
    return render_template('register_vendor.html')

@auth.route('/register_customer', methods=['GET', 'POST'])
def register_customer():
    return render_template('register_vendor.html')


@auth.route("/users", methods = ["POST", "GET"])
def user_list():
    #users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    users = User.query.order_by(User.date_created)
    #print(users) #prints query
    return render_template("user.html", users=users)

#logout only accessible if user logged in
@auth.route("/logout")
@login_required
def logout():
    #session.pop("user", None)
    logout_user()
    flash('Logged out successfully')
    return redirect(url_for('home.home_page'))

