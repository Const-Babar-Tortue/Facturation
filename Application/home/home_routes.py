from flask import render_template, request, make_response, Blueprint
from flask_login import login_required

from Application import db
from Application.models.FormModel import FormModel
from Application.models.users import User

home_bp = Blueprint("home_bp", __name__, template_folder="templates", static_folder="static")


@home_bp.route("/", methods=["GET"])
@login_required
def create_image():
    name = request.args.get("name")
    if name:
        existing_name = FormModel.query.filter(FormModel.name == name).first()
        if existing_name:
            return make_response(f"{name} already exist")
        new_form_model = FormModel(name=name)
        db.session.add(new_form_model)
        db.session.commit()

    forms = FormModel.query.all()
    users = User.query.all()
    return render_template("home.html", forms=forms, users=users, title="Show FormModel")
