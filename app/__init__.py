import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager ,AnonymousUserMixin

db = SQLAlchemy()
migrate = Migrate()
login_mng = LoginManager()
from config import Config
from flask import redirect,url_for,render_template,request
app =flask.Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:Refaa054614@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] ="powerful secretkey"

db.init_app(app)
migrate.init_app(app,db)
login_mng.init_app(app)

from app import models , views ,auth ,products ,special,edit


@app.shell_context_processor
def shell_ctx():
    return {
        "models":models,
        "User": models.User,
        "app":app,
        "db": db
    }

@login_mng.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)