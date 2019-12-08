import pytest
from mygame.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User(username='user', password_hash='asdf', blackscore=5, userscore=6, hardscore =10)
    return user

def test_score(new_user):
    assert new_user.blackscore == 5
    assert new_user.userscore == 6
    assert new_user.hardscore == 10
