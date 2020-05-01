from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from Application import db
from Application.models.ClientTable import Client

CREATE_PARSER = reqparse.RequestParser()
CREATE_PARSER.add_argument('name', type=str, required=True)
CREATE_PARSER.add_argument('street', type=str, required=True)
CREATE_PARSER.add_argument('streetNumber', type=str, required=True)
CREATE_PARSER.add_argument('postalCode', type=int, required=True)
CREATE_PARSER.add_argument('city', type=str, required=True)
CREATE_PARSER.add_argument('firm', type=bool, required=True)
CREATE_PARSER.add_argument('vatNumber', type=str, required=True)

DELETE_PARSER = reqparse.RequestParser()
DELETE_PARSER.add_argument('name', type=str, required=True)


class Clients(Resource):
    """ Class used for all API requests concerning clients"""

    method_decorators = [jwt_required()]

    @staticmethod
    def get():
        """Return all informations about all the clients"""

        clients = Client.query.all()

        parse_client = []

        for resp in clients:
            parse_client.append(build_item(resp))

        return jsonify(parse_client)

    @staticmethod
    def post():
        """Post a new client to the database"""

        args = CREATE_PARSER.parse_args()

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

    @staticmethod
    def delete():
        """Delete a client in the database"""

        args = DELETE_PARSER.parse_args()

        name = args['name']

        existing_client = Client.query.filter(
            Client.name == name
        ).first()

        if existing_client is None:
            response = jsonify({"message": "Client does not exists"})
            response.status_code = 404
            return response

        Client.query.filter(
            Client.name == name
        ).delete()
        db.session.commit()

        response = jsonify({'message': 'Deleted'})
        response.status_code = 200

        return response


def build_item(client):
    """A function used to help jsonify data for the get function"""

    client = {
        "name": client.name,
        "street": client.street,
        "streetNumber": client.street_number,
        "postalCode": client.postal_code,
        "city": client.city,
        "firm": client.firm,
        "vatNumber": client.vat_number
    }
    return client
