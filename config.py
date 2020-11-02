from app import db


class Config:
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = "database='postgres', user='postgres',password='Refaa054614'"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:Refaa054614@localhost:5432/postgres"