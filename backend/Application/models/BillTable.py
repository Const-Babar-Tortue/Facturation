from Application import db
from .ClientTable import Client
from .UserTable import User


class Bill(db.Model):
    __tablename__ = "Bills"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))

    # user = db.relationship('User', foreign_keys='Bills.user_id')
    # client = db.relationship('Client', foreign_keys='Bills.client_id')

    number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    expiration = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    cash = db.Column(db.Boolean, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
