import pytest
from mygame.models import User
import conftest
from mygame import app

#tests that the register page still loads even if the password isn't repeated
#correctly

def test_valid_login(client, db):

    response = client.post('/register',
                                data=dict(username='testing', password='testing', confirm ='test'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

    #assert b'Field must be equal to password.' in response.data

    #assert b'Invalid username or password' in response.data
    #print (response.data)
    #assert b"Congratulations, you are now a registered user!" in response.data
    #assert b'Hi !' in response.data
    #assert b'Log out' in response.data

@pytest.fixture
def client():
  client = app.test_client()
  return client
