from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from Application import db
from Application.models.BillTable import Bill

parser = reqparse.RequestParser()
parser.add_argument('username', type=int)
parser.add_argument('number', type=int)
parser.add_argument('date', type=str)
parser.add_argument('expiration_date', type=str)
parser.add_argument('price', type=float)
parser.add_argument('is_cash', type=bool)
parser.add_argument('is_paid', type=bool)


class Bills(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        bills = Bill.query.all()
        parse_bill = []

        for resp in bills:
            parse_bill.append(build_item(resp))

        return jsonify(parse_bill)

    def post(self):
        args = parser.parse_args()

        client = args['username']
        number = args['number']
        date = args['date']
        exp_date = args['expiratio_date']
        price = args['price']
        is_cash = args['is_cash']
        is_paid = args['is_paid']

        response = jsonify({"message": "Created"})
        response.status_code = 201
        return response


def calculate_vat(amount):
    return amount * .21


def total_with_vat(amount):
    return amount + calculate_vat(amount)

def build_item(bill):
    bill = {
        "client_id": bill.client_id,
        "number": bill.number,
        "date": bill.date,
        "expiration": bill.expiration,
        "price": bill.price,
        "cash": bill.cash,
        "paid": bill.paid
    }
    return bill
