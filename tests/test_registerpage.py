import pytest
from mygame.models import User
import conftest
from mygame import app

#tests that the register page redirects to the correct page after a user is created

def test_valid_register(client, db):

    response = client.post('/register',
                                data=dict(username='testing', password_hash='testing'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'Repeat Password' in response.data

@pytest.fixture
def client():
  client = app.test_client()
  return client
