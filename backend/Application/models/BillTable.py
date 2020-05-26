from Application import db
from .ClientTable import Client


class Bill(db.Model):
    __tablename__ = "Bills"

    id = db.Column(db.Integer, primary_key=True)

    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))

    subject = db.Column(db.String(256), nullable=False)
    date = db.Column(db.Date, nullable=False)
    expiration = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    cash = db.Column(db.Boolean, nullable=False)
    paid = db.Column(db.Boolean, nullable=False)
