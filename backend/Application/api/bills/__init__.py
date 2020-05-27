import dateutil.parser
from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from Application import db
from Application.models.BillTable import Bill

parser = reqparse.RequestParser()
parser.add_argument("clientId", type=str)
parser.add_argument("date", type=str)
parser.add_argument("expiration", type=str)
parser.add_argument("price", type=float)
parser.add_argument("cash", type=bool)
parser.add_argument("paid", type=bool)
parser.add_argument("subject", type=str)

delete_parser = reqparse.RequestParser()
delete_parser.add_argument("id", type=int, required=True)


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
        client_id = args["clientId"]
        date = dateutil.parser.isoparse(args["date"])
        expiration = dateutil.parser.isoparse(args["expiration"])
        price = args["price"]
        is_cash = args["cash"]
        is_paid = args["paid"]
        subject = args["subject"]

        bill = Bill(
            client_id=client_id,
            date=date,
            expiration=expiration,
            price=price,
            cash=is_cash,
            paid=is_paid,
            subject=subject,
        )

        db.session.add(bill)
        db.session.commit()

        response = jsonify({"message": "Created"})
        response.status_code = 201
        return response


def calculate_vat(amount):
    return amount * 0.21


def total_with_vat(amount):
    return amount + calculate_vat(amount)


def build_item(bill):
    bill = {
        "id": bill.id,
        "clientId": bill.client_id,
        "date": bill.date.isoformat(),
        "expiration": bill.expiration.isoformat(),
        "price": bill.price,
        "cash": bill.cash,
        "paid": bill.paid,
        "subject": bill.subject,
    }
    return bill
