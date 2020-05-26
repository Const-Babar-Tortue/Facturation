from flask import jsonify
from flask_jwt import current_identity
from flask_jwt import jwt_required
from flask_restful import Resource

from Application.models.UserTable import User


class Users(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        existing_user = User.query.filter(User.id == current_identity.id).first()

        if existing_user is None:
            response = jsonify({"message": "User doesn't exists anymore"})
            response.status_code = 410
            return response

        user = {"username": current_identity.username, "email": current_identity.email}

        return jsonify({"user": user})
