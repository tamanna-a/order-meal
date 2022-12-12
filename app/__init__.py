from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

from app.routes.home import home
from app.routes.profile import profile

app.register_blueprint(home)
app.register_blueprint(profile)



