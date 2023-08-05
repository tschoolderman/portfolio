from flask import redirect, render_template, request, url_for

from app.extensions import db
from app.models.question import Question
from app.questions import bp


@bp.route("/", methods=["GET", "POST"])
def index():
    questions = Question.query.all()

    # method on submit query
    if request.method == "POST":
        new_question = Question(
            content=request.form["content"], answer=request.form["answer"]
        )
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for("questions.index"))

    return render_template("questions/index.html", questions=questions)
