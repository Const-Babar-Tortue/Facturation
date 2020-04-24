from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)


class Bills(Resource):
    method_decorators = [jwt_required()]

    def post(self):
        response = jsonify({"message": "Created"})
        response.status_code = 201
        return response
