import flask_wtf
import wtforms
from wtforms import validators as vid

class Edit(flask_wtf.FlaskForm):

    description= wtforms.TextAreaField("Name", validators =[vid.DataRequired()],render_kw={"placeholder":"Set Description" })
    description2 = wtforms.TextAreaField("Name", validators=[vid.DataRequired()],render_kw={"placeholder": "Set Description"})
    description3 = wtforms.TextAreaField("Name", validators=[vid.DataRequired()],
                                         render_kw={"placeholder": "Set Description"})
    Sumbmit=  wtforms.SubmitField("Sign up")

