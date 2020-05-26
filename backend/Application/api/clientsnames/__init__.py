from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource

from Application.models.ClientTable import Client


class ClientsNames(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        clients = Client.query.all()

        response = []

        for client in clients:
            response.append(build_item(client))

        return jsonify(response)


def build_item(client):
    item = {
        'name': client.name,
        'id': client.id
    }

    return item
