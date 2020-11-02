from . import db
import flask_login

class Edit(db.Model, flask_login.UserMixin):
    __tablename__ = 'aboutus'
    id = db.Column(db.INTEGER(),primary_key=True)
    des = db.Column(db.String(255))
    des2 =db.Column(db.String(255))
    des3 = db.Column(db.String(255))

    def __init__(self , des , des2,des3):
        self.des =des.title()
        self.des2 = des2.title()
        self.des3 = des2.title()






