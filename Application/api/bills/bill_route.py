from flask import Blueprint, jsonify
from flask_jwt import jwt_required, current_identity

from Application.models.BillTable import Bill

bill_api_bp = Blueprint("bill_api_bp", __name__)


# list bills
@bill_api_bp.route("/bill", methods=["GET"])
@jwt_required()
def bill():
    user_id = current_identity.id
    results = Bill.query.filter(Bill.user_id == user_id).all()

    # date = datetime.datetime.now().date()
    # babar = Bill(id=1, user_id=1, client_id=1, number=1,
    #              date=date, expiration=date, price=1, cash=True, paid=False)
    # db.session.add(babar)
    # db.session.commit()

    response = list()
    for res in results:
        item = {
            'number': res.number,
            'date': res.date,
            'expiration': res.expiration,
            'price': res.price,
            'paid': res.paid
        }
        response.append(item)

    return jsonify(response)
