from flask_jwt import jwt_required
from flask_restful import Resource

from Application import db
from Application.models.BillTable import Bill
from Application.models.ClientTable import Client


class SingleClient(Resource):
    method_decorators = [jwt_required()]

    def delete(self, client_id):
        exists = Client.query.filter(Client.id == client_id).first()

        if exists is None:
            return {"message": "Client does not exists"}, 404

        # delete all bills related to this client
        Bill.query.filter(Bill.client_id == client_id).delete()

        Client.query.filter(Client.id == client_id).delete()
        db.session.commit()

        return {"message": "Deleted"}