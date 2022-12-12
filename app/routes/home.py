from flask import Blueprint

home = Blueprint('name', __name__)

@home.route('/')
def home_page():
    """the home page"""
    return render_template('home.html')