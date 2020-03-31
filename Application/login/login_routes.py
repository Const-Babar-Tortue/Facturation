from flask import render_template, request, Blueprint, url_for, redirect, flash
from flask_login import current_user, login_user

from Application import login_manager
from Application.forms.LoginForm import LoginForm
from Application.models.UserTable import User

login_bp = Blueprint("login_bp", __name__, template_folder="templates", static_folder="static")


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))

    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            email = request.form.get("email")
            password = request.form.get("password")
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password=password):
                login_user(user)
                return redirect(url_for("home_bp.home"))
        flash("Invalid username/password")
        return redirect(url_for("contact_bp.contact"))

    return render_template("login.html", form=form, title="Log in.")


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view that page.")
    return redirect(url_for("login_bp.login"))
