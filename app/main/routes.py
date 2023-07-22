from flask import flash, redirect, render_template, request, url_for

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
            return "Form posted"
        else:
            return render_template("contact.html", form=form)

    return render_template("contact.html", form=form)


@bp.route("/magic/", methods=["GET", "POST"])
def magic():
    if request.method == "POST":
        return redirect(url_for("main.dashboard"))
    else:
        return render_template("magic.html")


@bp.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")
