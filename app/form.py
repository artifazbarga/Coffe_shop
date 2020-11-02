import flask_wtf
import wtforms
import cgi
from wtforms import validators as vid

class SignupForm(flask_wtf.FlaskForm):

    username= wtforms.StringField("Name", validators =[vid.Length(min=4, max=25)],render_kw={"placeholder":"Name" })
    password= wtforms.PasswordField("Password" ,validators=[vid.DataRequired()],render_kw={"placeholder":"Password"})
    PhoneNumber = wtforms.IntegerField("Phone Number",validators= [vid.DataRequired()] , render_kw={"placeholder":"Phone number"})
    email = wtforms.StringField("Email",validators =[vid.DataRequired()], render_kw={"placeholder": "Email"})
    Sumbmit=  wtforms.SubmitField("Sign up")


class QueryForm(flask_wtf.FlaskForm):
    query = wtforms.StringField("")
    submit= wtforms.SubmitField("search")