from flask_restful import Resource
from flask_jwt import jwt_required

from Application import db
from Application.models.BillTable import Bill


class SingleBill(Resource):
    method_decorators = [jwt_required()]

    def delete(self, bill_id):
        exists = Bill.query.filter(Bill.id == bill_id).first()

        if exists is None:
            return {"message": "Bill does not exists"}, 404

        Bill.query.filter(Bill.id == bill_id).delete()
        db.session.commit()

        return {"message": "Deleted"}
