from Application import db
from .UserTable import User


class Client(db.Model):
    __tablename__ = "Clients"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(256), nullable=False)
    street_number = db.Column(db.String(6), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(256), nullable=False)

    firm = db.Column(db.Boolean, nullable=True)
    vat_number = db.Column(db.String(20), nullable=True)
