from datetime import datetime
from mygame import db
from mygame import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

"""
models.py
=======================================
sets the data base coloumns for the user2
"""

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    userscore = db.Column(db.Integer, default=0)
    blackscore = db.Column(db.Integer, default=0)
    hardscore = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        """
        sets the password for the user based on what the user entered and hashes it for security

        Parameters
        ----------
        password
            the string of the user's password
        """

        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        """
        a function for when the password needs to be checked

        Parameters
        ----------
        password
            the string of the user's password
        """

        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Posts {}>'.format(self.body)



@login.user_loader
def load_user(id):
    """
    loads the user if the credentials are right

    Parameters
    ----------
    id
        id of the user
    """

    return User.query.get(int(id))
