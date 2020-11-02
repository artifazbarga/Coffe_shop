from . import db
from .utils import ModelMixin

class Products(db.Model,ModelMixin):
    __tablename__ = 'products'
    # id = db.Column(db.INTEGER(),primary_key=True)
    name = db.Column(db.String(64) ,nullable=False)
    price = db.Column(db.INTEGER() ,nullable=False)
    des = db.Column(db.String(255))
    image = db.Column(db.String(255) , nullable=False)
    kind = db.Column(db.INTEGER(), nullable=False)

    def __init__(self, name, price , des , image ,kind):
        self.name = name.title()
        self.price = price
        self.des =des.title()
        self.image = image
        self.kind =kind




    def __repr__(self):
        return f"<User {self.id}.{self.name}"

