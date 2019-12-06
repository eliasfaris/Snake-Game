import pytest
from mygame.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User(username='user', password_hash='asdf')
    return user

def test_user(new_user):
    assert new_user.username == 'user'
    #assert new_user.hashed_password != 'asdf'
    assert new_user.password_hash == 'asdf'
    #assert not new_user.authenticated
    #assert new_user.role == 'user'
