import pytest
from mygame.models import User
from mygame import db

#tests that a user can be correctly added to the database

def test_add_user_to_db(db):
    user1 = User(username='john', password_hash='test')
    db.session.add(user1)
    db.session.commit()
    assert len(User.query.all()) == 1
