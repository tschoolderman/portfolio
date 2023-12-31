from configobj import ConfigObj
from flask import redirect, render_template, request, url_for
from flask_mail import Message

from app.extensions import mail
from app.main import bp
from app.models.contactform import ContactForm

config = ConfigObj(".flaskenv")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    if request.method == "POST":
        if form.validate():
            msg = Message(
                form.subject.data,
                sender="contact@example.com",
                recipients=[config["FLASK_MAIL_RECIPIENT"]],
            )
            msg.body = """From: %s -- %s\n\n%s""" % (
                form.name.data,
                form.email.data,
                form.message.data,
            )
            mail.send(msg)
            return redirect(url_for("main.contact_succes"))
        else:
            return render_template("index.html", form=form)
    elif request.method == "GET":
        return render_template("index.html", form=form)


@bp.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate():
            msg = Message(
                form.subject.data,
                sender="contact@example.com",
                recipients=[config["FLASK_MAIL_RECIPIENT"]],
            )
            msg.body = """From: %s -- %s\n\n%s""" % (
                form.name.data,
                form.email.data,
                form.message.data,
            )
            mail.send(msg)
            return redirect(url_for("main.contact_succes"))
        else:
            return render_template("contact.html", form=form)
    elif request.method == "GET":
        return render_template("contact.html", form=form)


@bp.route("/contact/succes")
def contact_succes():
    return render_template("contact.succes.html")


@bp.route("/magic/", methods=["GET", "POST"])
def magic():
    if request.method == "POST":
        return redirect(url_for("main.dashboard"))
    else:
        return render_template("magic.html")


@bp.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")
