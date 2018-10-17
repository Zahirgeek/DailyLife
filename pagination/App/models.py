from App.ext import db


class User(db.Model):

    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    u_name = db.Column(db.String(16), unique=True)
    u_age = db.Column(db.Integer, default=1)