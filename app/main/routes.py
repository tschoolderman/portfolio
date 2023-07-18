from flask import redirect, render_template, request, url_for

from app.main import bp


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/magic", methods=["GET", "POST"])
def magic():
    if request.method == "POST":
        return redirect(url_for("main.dashboard"))
    else:
        return render_template("magic.html", title="Magic")


@bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")
