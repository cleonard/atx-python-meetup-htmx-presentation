import re

from app import db

RE_NON_WORD = re.compile(r"\W+")
TOKEN_LEN = 6


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

    @property
    def handle(self):
        handle_text = RE_NON_WORD.sub("", self.author)
        return f"@{handle_text}"

    @property
    def created_display(self):
        return self.created_at.strftime("%e %b").strip()
