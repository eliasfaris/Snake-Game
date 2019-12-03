import pytest
from mygame.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User('user','asdf')
    return user

def test_user(new_user):
    assert new_user.username == 'user'
    assert new_user.hashed_password != 'asdf'
    assert not new_user.authenticated
    assert new_user.role == 'user'

"""
if __name__ == '__main__':
    unittest.main()
"""
