from app import db
from app.models.user import User


found_user =  User.query.all()