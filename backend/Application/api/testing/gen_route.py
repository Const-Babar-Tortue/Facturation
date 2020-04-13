from flask import Blueprint, jsonify
from flask_jwt import jwt_required, current_identity
import datetime

from Application.models.ClientTable import Client
from Application.models.BillTable import Bill
from Application import db

gen_api_bp = Blueprint("gen_api_bp", __name__)


# Gen some data // TODO remove me when a webpage is implemented
@gen_api_bp.route("/gen", methods=["GET"])
@jwt_required()
def gen():
    user_id = current_identity.id

    michel = Client(
        name="Michel",
        street="Rue de la tour",
        street_number="42",
        postal_code=1495,
        city="Villers-la-Ville",
        firm=False,
        vat_number="babar"
    )

    db.session.add(michel)
    db.session.commit()

    date = datetime.datetime.now().date()
    michel_first_bill = Bill(user_id=user_id, client_id=michel.id, number=1,
                            date=date, expiration=date, price=300, cash=True, paid=False)

    michel_second_bill = Bill(user_id=user_id, client_id=michel.id, number=2,
                              date=date, expiration=date, price=1.5, cash=False, paid=True)

    db.session.add(michel_first_bill)
    db.session.add(michel_second_bill)

    babar = Client(
        name="Babar",
        street="Avenue du Ciseau",
        street_number="42",
        postal_code=1348,
        city="Louvain-la-Neuve",
        firm=False,
        vat_number="babar"
    )

    db.session.add(babar)
    db.session.commit()

    babar_first_bill = Bill(user_id=user_id, client_id=babar.id, number=1,
                            date=date, expiration=date, price=300, cash=True, paid=False)

    db.session.add(babar_first_bill)
    db.session.commit()

    return jsonify("Created")
