import flask_wtf
import wtforms
from wtforms import validators as vid

class Addcart(flask_wtf.FlaskForm):

    name= wtforms.StringField("Name", validators =[vid.DataRequired()],render_kw={"placeholder":"Name of product" })
    price= wtforms.IntegerField("price" ,validators=[vid.DataRequired()],render_kw={"placeholder":"Price of product"})
    des = wtforms.StringField("Description" , render_kw={"placeholder":"Description of product"})
    image = wtforms.StringField("url_image",validators =[vid.DataRequired()], render_kw={"placeholder": "URl image for product"})
    kind = wtforms.IntegerField("kind", validators=[vid.DataRequired()],
                                 render_kw={"placeholder": "1-ice,2-hot,3-fruit"})
    phone = wtforms.IntegerField("kind", validators=[vid.DataRequired()],
                                render_kw={"placeholder": "1-ice,2-hot,3-fruit"})
    Sumbmit=  wtforms.SubmitField("Sign up")


class QueryForm(flask_wtf.FlaskForm):
    query = wtforms.StringField("")
    submit= wtforms.SubmitField("search")