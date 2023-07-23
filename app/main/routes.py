from os import environ

from flask import redirect, render_template, request, url_for
from flask_mail import Message

from app.extensions import mail
from app.main import bp
from app.main.contactform import ContactForm


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate():
            msg = Message(
                form.subject.data,
                sender="contact@example.com",
                recipients=[environ.get("FLASK_MAIL_RECIPIENT")],
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
