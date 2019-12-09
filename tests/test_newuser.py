import pytest
from mygame.models import User

#tests that models.py correctly stores username and password data

@pytest.fixture(scope='module')
def new_user():
    user = User(username='user', password_hash='asdf')
    return user

def test_user(new_user):
    assert new_user.username == 'user'
    assert new_user.password_hash == 'asdf'
