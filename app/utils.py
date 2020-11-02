from app import db
import datetime

class ModelMixin:
    id = db.Column(db.INTEGER() , primary_key=True)
    create_at = db.Column(db.TIMESTAMP ,default= datetime.datetime.now())
    update_at = db.Column(db.TIMESTAMP, onupdate= datetime.datetime.now())


    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            print("Error on save of",self)
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
