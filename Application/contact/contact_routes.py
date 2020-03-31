from flask import render_template, Blueprint, url_for, redirect

from Application.forms.ContactForm import ContactForm

contact_bp = Blueprint("contact_bp", __name__, template_folder="templates", static_folder="static")


@contact_bp.route("/contact", methods=("GET", "POST"))
def contact():
    form = ContactForm()
    if form.validate():
        return redirect(url_for("success"))
    return render_template("contact_form.html", form=form)
