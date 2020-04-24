from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource

from Application.models.ClientTable import Client


class GetNameClient(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        names_client = Client.query.with_entities(Client.name)

        parse_name_client = list()

        for resp in names_client:
            parse_name_client.append(build_item(resp))

        return jsonify(parse_name_client)


def build_item(client):
    name = client.name
    return name
