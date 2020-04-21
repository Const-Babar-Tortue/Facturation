from flask import jsonify
from flask_jwt import current_identity, jwt_required
from flask_restful import Resource, reqparse

from Application import db
from Application.models.ClientTable import Client

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('street', type=str, required=True)
parser.add_argument('streetNumber', type=str, required=True)
parser.add_argument('postalCode', type=int, required=True)
parser.add_argument('city', type=str, required=True)
parser.add_argument('firm', type=bool, required=True)
parser.add_argument('vatNumber', type=str, required=True)


class Clients(Resource):
    # method_decorators = [jwt_required()]

    def post(self):
        args = parser.parse_args()

        name = args['name']

        exists = Client.query.filter(
            (Client.name == name)
        ).first()

        if exists:
            response = jsonify({"message": "Client already exists"})
            response.status_code = 409
            return response

        street = args['street']
        street_number = args['streetNumber']
        postal_code = args['postalCode']
        city = args['city']
        firm = args['firm']
        vat_number = args['vatNumber']

        client = Client(
            name=name,
            street=street,
            street_number=street_number,
            postal_code=postal_code,
            city=city,
            firm=firm,
            vat_number=vat_number
        )

        db.session.add(client)
        db.session.commit()

        response = jsonify({'message': 'Created'})
        response.status_code = 201

        return response
