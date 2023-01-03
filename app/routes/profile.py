from flask import Blueprint

profile = Blueprint('name', __name__)

@profile.route('/profile')
def profile_page():
    """the home page"""
    #return render_template('profile.html')
    return