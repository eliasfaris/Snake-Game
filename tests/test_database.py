import pytest
from mygame.models import User
from mygame import db

@pytest.fixture(scope='module')
def init_database():

    db.create_all()

    user1 = User(username='ryota', plaintext_password='password1')
    user2 = User(username='elias', plaintext_password='password2')
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db

    db.drop_all()
