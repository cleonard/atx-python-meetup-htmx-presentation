"""Cleans out posts and creates seed posts in the database"""

from app import db
from app.models import Post
from app.fake import generate_post


def seed(num=3):
    # Clean out existing posts
    deleted = Post.query.delete()
    print(f"{deleted} posts deleted.")

    # Create `num` number of posts
    for _ in range(num):
        post_data = generate_post()
        post = Post(**post_data)
        db.session.add(post)

    db.session.commit()
