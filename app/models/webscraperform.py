from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class WebscraperForm(FlaskForm):
    url = StringField("url")
    submit = SubmitField("Send")
