from flask import render_template

# from app.extensions import db
from app.models.post import Post
from app.posts import bp


@bp.route("/")
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)


@bp.route("/categories/")
def categories():
    return render_template("posts/categories.html")


@bp.route("/<int:post_id>/")
def single_post(post_id):
    single_post = Post.query.get_or_404(post_id)
    return render_template("posts/single_post.html", single_post=single_post)
