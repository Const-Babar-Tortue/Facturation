from wtforms import StringField, SubmitField, Form, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


class SignInForm(Form):
    name = StringField("Name", [DataRequired()])
    email = StringField(
        "Email",
        [
            DataRequired(),
            Length(min=6, message="Please enter a valid email address."),
            Email(message="Please enter a valid email address."),
        ],
    )
    password = PasswordField(
        "Password",
        [
            DataRequired(),
            Length(min=6, message="Please select a stronger password."),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm your password.")
    website = StringField("Website", [Optional()])
    submit = SubmitField("Register")
