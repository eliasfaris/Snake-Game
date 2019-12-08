import pytest
import os

TESTDB = 'test_app.db'
TESTDB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), TESTDB)
TESTDB_URI = 'sqlite:///' + TESTDB_PATH

@pytest.fixture(scope='module')
def app():
    from mygame import create_app
    app = create_app({'TESTING' : True,
        'SQLALCHEMY_DATABASE_URI' : TESTDB_URI,
        'SQLALCHEMY_TRACK_MODIFICATIONS':  False,
        'SECRET_KEY' : 'test'
        })

    return app

@pytest.fixture(scope='module')
def app_context(app):
    with app.app_context():
        yield app

@pytest.fixture(scope='module')
def client(app_context):
    return app_context.test_client()


@pytest.fixture(scope='module')
def db(app_context):

    from mygame.models import User
    from mygame import db
    db.create_all()

    yield db

    db.drop_all()
    os.unlink(TESTDB_PATH)
