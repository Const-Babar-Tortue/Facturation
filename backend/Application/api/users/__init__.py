from flask import jsonify
from flask_jwt import current_identity
from flask_restful import Resource

from Application import db
from Application.models.UserTable import User

from flask_jwt import jwt_required

class Users(Resource):
	method_decorators=[jwt_required()]

	def get(self):
		user = {
			'username' : current_identity.username,
			'email' : current_identity.email
		}

		user_list=[user]

		return jsonify(user_list)