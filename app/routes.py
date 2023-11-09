"""Authentication routes"""

from flask import Blueprint, render_template, redirect, request, url_for

from app import db, fake
from app.models import Post
from app.seed import seed

bp = Blueprint("blog", __name__, url_prefix="/")


@bp.route("/")
def home():
    page_title = "Home"
    posts = Post.query.order_by(Post.created_at.desc())
    return render_template("home.html", page_title=page_title, posts=posts)


@bp.route("/post", methods=["POST",])
def post():
    # Create and save post
    content = request.form.get("post-content")
    author = fake.author()
    post = Post(content=content, author=author)
    db.session.add(post)
    db.session.commit()

    html = render_template("fragments/post.html", post=post)
    return html


@bp.route("/seed")
def seed_db():
    """This method is for demo purposes, clears out the database and adds some
    placeholder posts
    """
    seed()
    return redirect(url_for("blog.home"))
