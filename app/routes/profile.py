from flask import Blueprint

profile = Blueprint('name', __name__)

@profile.route('/')
def profile_page():
    """the home page"""
    return render_template('profile.html')