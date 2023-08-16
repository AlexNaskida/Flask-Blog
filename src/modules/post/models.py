from src.extensions.database import PkModel, db
from datetime import datetime


class Post(PkModel):
    slug =  db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes = db.relationship('PostLike', backref='post', lazy='dynamic')
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class PostLike(PkModel):
    __tablename__ = 'post_like'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
