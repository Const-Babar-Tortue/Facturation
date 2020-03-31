from flask import Blueprint, jsonify
from collections import namedtuple

from Application.models.BillTable import Bill

bill_api_bp = Blueprint("bill_api_bp", __name__)

Bill_Item = namedtuple('Bill', 'number date expiration price cash paid')


# list bills
@bill_api_bp.route("/bill", methods=["GET"])
def bill():
    results = Bill.query.all()
    return jsonify(results)
