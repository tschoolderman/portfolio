from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired(message="Please enter your name")]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(message="Please enter your email adress"), Email()],
    )
    subject = StringField(
        "Subject", validators=[DataRequired(message="Please enter a subject")]
    )
    message = TextAreaField(
        "Message", validators=[DataRequired(message="Please enter a message")]
    )
    submit = SubmitField("Send")
