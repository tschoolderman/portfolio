from flask import redirect, render_template, request, url_for

from app.extensions import db
from app.models.post import Post
from app.posts import bp


@bp.route("/")
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@bp.route("/<int:post_id>/")
def single_post(post_id):
    single_post = Post.query.get_or_404(post_id)
    return render_template("posts/single_post.html", single_post=single_post)


@bp.route("/edit/<int:post_id>/", methods=["POST"])
def edit_post(post_id):
    new_title = request.form.get("title")
    new_content = request.form.get("content")

    get_post = Post.query.get_or_404(post_id)

    if get_post:
        get_post.title = new_title
        get_post.content = new_content

        db.session.commit()

        return redirect(url_for("posts.index"))
    else:
        return 404


@bp.route("/new/", methods=["POST"])
def new_post():
    new_post = Post(
        title=request.form["title"],
        content=request.form["content"],
    )
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("posts.index"))


@bp.route("/delete/<int:post_id>/", methods=["GET", "POST"])
def delete_post(post_id):
    get_post = Post.query.get_or_404(post_id)

    if get_post:
        db.session.delete(get_post)
        db.session.commit()
        return redirect(url_for("posts.index"))
    else:
        return 404
