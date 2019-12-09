import pytest
from mygame.models import User
from mygame import app

#tests that a page loads on route /
#response code 302 is desired because we want the page to auto redirect to
#either to login or color picker if the user is remembered

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 302

@pytest.fixture
def client():
  client = app.test_client()
  return client
