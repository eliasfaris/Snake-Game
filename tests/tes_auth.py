import pytest
from mygame.models import User


def test_get_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Email' in response.data
    assert b'Password' in response.data


def test_add_user_to_db(db):
    user1 = User(username='john', password_hash='test')
    db.session.add(user1)
    db.session.commit()
    assert len(User.query.all()) == 1


def test_valid_register(db):

    response = client.post('/register',
                                data=dict(username='testing', password='testing'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"You are now logged in!" in response.data
    #assert b'Hi !' in response.data
    assert b'Log out' in response.data
