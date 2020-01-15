import base64, hashlib, binascii

from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from config import START_ID

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_urole(self):
        return self.urole


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    slug = db.Column(db.String(64), unique=True)
    content = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return '<Post {} : {}>'.format(self.title, self.content)

    def update_slug(self):
        global START_ID
        self.slug = hashlib.sha1(START_ID.encode('utf-8')).hexdigest()
        START_ID += 1

    def update_slug_static(self, numb):
        self.slug = hashlib.sha1(numb.encode('utf-8')).hexdigest()

    def update_slug_hash(self, password):
        self.slug = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), b'very-smart-salt', 10000)).decode()
