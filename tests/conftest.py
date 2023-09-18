import pytest


from currencies import create_app, db
from currencies.config import testing
from currencies.models import *
from currencies.router import currency_blueprint


@pytest.fixture
def app():
    app = create_app(testing)
    app.register_blueprint(currency_blueprint, url_prefix="/api/v1")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db_test(app):
    with app.app_context():
        yield db