from flask import Blueprint, jsonify, request, flash
from flask_jwt import jwt_required, current_identity

from Application.models.BillTable import Bill
from Application.models.ClientTable import Client

bill_api_bp = Blueprint("bill_api_bp", __name__)


# list bills for logged in user
@bill_api_bp.route("/bill", methods=["GET"])
@jwt_required()
def bill():
    user_id = current_identity.id

    results = Bill.query.filter(Bill.user_id == user_id)

    paid_filter = request.args.get("paid", None)

    if paid_filter is None:
        pass
    else:
        paid = True if paid_filter in ["True", "true", "1"] else False
        results = results.filter(Bill.paid == paid)

    client_filter = request.args.get("client", None)
    if client_filter is not None:
        client = Client.query.filter(Client.name == client_filter).first()
        results = results.filter(Bill.client_id == client.id)

    results = results.all()

    response = list()
    for res in results:
        item = _build_item(res)
        response.append(item)

    return jsonify(response)


def _build_item(bill):
    client_id = bill.client_id
    client = Client.query.filter(Client.id == client_id).first()

    client_dict = {
        'name': client.name,
        'street': client.street,
        'street_number': client.street_number,
        'postal_code': client.postal_code,
        'city': client.city,
        'vat_number': client.vat_number
    }

    item = {
        'date': bill.date,
        'expiration': bill.expiration,
        'price': bill.price,
        'paid': bill.paid,
        'client': client_dict
    }

    return item
