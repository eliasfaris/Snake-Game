import pytest
from mygame.models import User
from mygame import db

def test_add_user_to_db(db):
    user1 = User(username='john', password_hash='test')
    db.session.add(user1)
    db.session.commit()
    assert len(User.query.all()) == 1
