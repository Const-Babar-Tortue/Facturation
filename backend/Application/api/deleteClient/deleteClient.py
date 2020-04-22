from datetime import datetime

from flask import jsonify
from flask_jwt import current_identity
from flask_restful import Resource, reqparse

from Application import db
from Application.models.ClientTable import Client

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class DeleteClient(Resource):
	def post(self):
		name = args['name']

		existing_client = Client.query.filter(
			Client.name == name
		).first()

		if !existing_client:
			reponse = jsonify({"message": "Client does not exists"})
			response.status_code = 404
			return response

		Client.query.filter(
			Client.name == name
		).delete()
		db.session.commit()
