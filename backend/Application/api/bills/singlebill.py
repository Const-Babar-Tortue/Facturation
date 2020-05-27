from flask_jwt import jwt_required
from flask_restful import Resource

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

    def patch(self, bill_id):
        selected_bill = Bill.query.filter(Bill.id == bill_id).first()

        if selected_bill is None:
            return {"message": "Bill does not exists"}, 404

        selected_bill.paid = not selected_bill.paid
        db.session.commit()

        message = "Bill is now paid" if selected_bill.paid else "Bill is unpaid"
        return {"message": message}
