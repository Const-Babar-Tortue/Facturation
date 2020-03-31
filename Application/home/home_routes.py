from flask import render_template, Blueprint
from flask_login import login_required

from Application.models.UserTable import User

home_bp = Blueprint("home_bp", __name__, template_folder="templates", static_folder="static")


@home_bp.route("/", methods=["GET"])
@login_required
def create_image():
    users = User.query.all()
    return render_template("home.html", users=users, title="Show FormModel")
