import flask_wtf
import wtforms
from wtforms import validators as vid

class SignupFormlogin(flask_wtf.FlaskForm):

    PhoneNumber = wtforms.IntegerField("Phone Number", validators=[vid.DataRequired()],render_kw={"placeholder": "Phone number"})
    password= wtforms.PasswordField("Password" ,validators=[vid.DataRequired()],render_kw={"placeholder":"Password"})

    Sumbmit=  wtforms.SubmitField("Sign up")
