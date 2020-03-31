from flask import Blueprint, jsonify
from flask_jwt import jwt_required

from Application.models.BillTable import Bill

bill_api_bp = Blueprint("bill_api_bp", __name__)


# list bills
@bill_api_bp.route("/bill", methods=["GET"])
@jwt_required()
def bill():
    results = Bill.query.all()
    return jsonify(results)
