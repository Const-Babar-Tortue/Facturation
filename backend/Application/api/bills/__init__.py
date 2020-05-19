from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from Application import db
from Application.models.BillTable import Bill
from Application.models.ClienTable import Client

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('number', type=int)
parser.add_argument('date', type=str)
parser.add_argument('expiration', type=str)
parser.add_argument('price', type=float)
parser.add_argument('is_cash', type=bool)
parser.add_argument('is_paid', type=bool)

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('number', type=int, required=True)

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

        client_name = args['username']

        client = Client.query.filter(
            (Client.name == client_name)
        )

        client_id = client.id
        number = args['number']
        date = args['date']
        exp_date = args['expiration']
        price = args['price']
        is_cash = args['is_cash']
        is_paid = args['is_paid']

        bill = Bill(
            client_id = client_id,
            number = number,
            date = date,
            expiration = exp_date,
            price = price,
            cash = is_cash,
            paid = is_paid
        )

        db.session.add(bill)
        db.session.commit()

        response = jsonify({"message": "Created"})
        response.status_code = 201
        return response

    def delete(self):
        args = delete_parser.parse_args()

        number = args["number"]

        existing_bill = Bill.query.filter(
            Bill.number == number
        ).first()

        if existing_bill is None:
            response = jsonify({"message": "Bill does not exists"})
            response.status_code = 404
            return response
        
        Bill.query.filter(
            Bill.number ==number
        ).delete()
        db.session.commit()

        response = jsonify({'message': 'Deleted'})
        response.status_code = 200

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
