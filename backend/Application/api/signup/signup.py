from datetime import datetime

from flask import jsonify
from flask_jwt import jwt_required, current_identity
from flask_restful import Resource, reqparse

from Application import db
from Application.models.UserTable import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('email', type=str)
parser.add_argument('password', type=str)


class Signup(Resource):
    # decorators = [jwt_required()]

    def post(self):
        print(current_identity)
        args = parser.parse_args()

        username = args['username']
        email = args['email']
        password = args['password']

        existing_user = User.query.filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            response = jsonify({"message": "User already exists"})
            response.status_code = 409
            return response

        user = User(
            username=username,
            email=email,
            created_on=datetime.now()
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        response = jsonify({"message": "Created"})
        response.status_code = 201
        return response
