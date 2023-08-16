import os
from flask import Flask
from src.extensions.database import PkModel, db
from src.modules.post.models import Post, PostLike
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user


class User(PkModel, UserMixin):
    __tablename__ = "users"

    name =  db.Column(db.String(60))
    lastname =  db.Column(db.String(60))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('src.modules.post.models.Post', backref='poster')
    liked = db.relationship('src.modules.post.models.PostLike', foreign_keys='PostLike.user_id', backref='user', lazy='dynamic')

    def like_post(self, post):
        if not self.has_liked_post(post):
            like = PostLike(user_id=self.id, post_id=post.id)
            db.session.add(like)

    def unlike_post(self, post):
        if self.has_liked_post(post):
            PostLike.query.filter_by(
                user_id=self.id,
                post_id=post.id).delete()

    def has_liked_post(self, post):
        return PostLike.query.filter(
            PostLike.user_id == self.id,
            PostLike.post_id == post.id).count() > 0

    # @property
    # def password(self):
    #     raise AttributeError('password is not a readable attribute')

    # @password.setter
    # def password(self, password):
    #     self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Name {self.name}>'

