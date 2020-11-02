from app import form ,formlogin
from flask import session
from . import *
from app import app
from app.models import User
import sys
import flask_login

@app.route('/login' ,methods=['GET','POST'])
def login():
    Form = formlogin.SignupFormlogin()
    if request.method == 'POST':
        #check username and password is th same true? login
        number = 546147282
        user = User.login_user(Form.PhoneNumber.data,Form.password.data)
        # user = User.query.filter_by(phonenumber = Form.PhoneNumber.data , password = Form.password.data).first()
        if user:
            session['admin'] = Form.PhoneNumber.data
            return flask.redirect(url_for('homePAge'))
    # if session['admin'] != None:
    #     return flask.redirect(url_for('Profile'))
    return flask.render_template('login.html',form=Form )


@app.route('/signup' ,methods=["GET","POST"])
def signup():
    Form=  form.SignupForm()
    db.create_all()
    db.session.commit()
    Form.validate()
    if flask.request.method == "POST":
        if Form.username.data != None and Form.password.data != None and Form.PhoneNumber.data != None:
            user = User(Form.username.data,Form.password.data,Form.PhoneNumber.data,Form.email.data)
            try :
                user.save()
                # db.session.add(user)
                # db.session.commit()
            except Exception as e:
                print(str(e.args)[120:][:-5])
                return flask.render_template("signup.html", form=Form, e =str(e.args)[120:][:-5])
            except:
                print("Unexpected error:", sys.exc_info()[0])
                return flask.render_template("signup.html", form=Form, e=sys.exc_info()[0])
            return flask.redirect(url_for('login'))
    return flask.render_template("signup.html" , form =Form)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flask.session['admin'] =''
    return flask.redirect('/')

@app.route('/Profile/<phone>')
def Profile(phone):
    pass