import pytest
from mygame.models import User
import conftest
from mygame import app

def test_valid_register(client, db):

    response = client.post('/register',
                                data=dict(username='testing', password_hash='testing'),
                                follow_redirects=True)
    assert response.status_code == 200
    #print (response.data)
    #assert b"Congratulations, you are now a registered user!" in response.data
    #assert b'Hi !' in response.data
    #assert b'Log out' in response.data

@pytest.fixture
def client():
  client = app.test_client()
  return client
