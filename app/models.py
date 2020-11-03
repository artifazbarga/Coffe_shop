from . import db
import flask_login
from .utils import ModelMixin
class User(db.Model,ModelMixin ,flask_login.UserMixin ):
    __tablename__ = 'users'
    # id = db.Column(db.INTEGER(),primary_key=True)
    name = db.Column(db.String(64) ,nullable=False)
    password = db.Column(db.String(64) ,nullable=False)
    phonenumber = db.Column(db.INTEGER() ,unique=True)
    email = db.Column(db.String(255))

    def __init__(self, name, password , phonenumber , email):
        self.name = name.title()
        self.password = password.title()
        self.phonenumber =phonenumber
        self.email = email.lower()
        self.set_password(password)


    def set_password(self, password):
        self.pwdhash = (password)

    def check_password(self, password):
        return password


    @classmethod
    def login_user(cls ,phonenumber, password):
        user_l = cls.query.filter_by(phonenumber = phonenumber).first()
        if user_l and user_l.check_password(password):
            flask_login.login_user(user_l)
            return user_l
        return False
    @classmethod
    def get_phone(cls):
        return cls.phonenumber

    def __repr__(self):
        return f"<User {self.id}.{self.name}"


