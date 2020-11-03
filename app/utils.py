from app import db
import datetime

class ModelMixin:
        id = db.Column(db.Integer(), primary_key=True)
        created_at = db.Column(db.DateTime, default=datetime.datetime.now)
        updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

        def save(self):
            db.session.add(self)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Error on save of",e)
        def delete(self):
            db.session.delete(self)
            try:
                db.session.commit()
                print("deleted")
            except:
                db.session.rollback()
                print("Error on delete of",self)

        def update(self):
            db.session.add(self)
            try:
                db.session.commit()
            except:
                db.session.rollback()
                print("Error on update of", self)
