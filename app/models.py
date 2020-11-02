from . import db
import flask_login
class User(db.Model, flask_login.UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER(),primary_key=True)
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

    def get_phonenumber(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.phonenumber


