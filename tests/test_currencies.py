from currencies import crud
from tests.conftest import db
from currencies.models import Currencies

def test_get_currencies_history(client):
    currencies_data = [
        {"code": "USD", "price": 1.0},
        {"code": "EUR", "price": 0.85},
        {"code": "GBP", "price": 0.75},
    ]
    for data in currencies_data:
        crud.create_currency(db=db, currency_data=data)

    response = client.get('/api/v1/currencies/history')

    assert response.status_code == 200


def test_get_currency_value(client):
    currency_code = "USD"
    response = client.get(f"/api/v1/currencies/{currency_code}")

    assert response.status_code == 200

    data = response.get_json()
    assert currency_code in data.values()


def test_create_currency(client):

    currency_data = {"code": "CAD", "price": 1.25}

    result = crud.create_currency(db, currency_data)
    db.session.commit()


    currency = Currencies.query.filter(Currencies.code == currency_data.get("code"))[0]
    assert currency is not None
    assert currency.price == currency_data["price"]


def test_create_duplicate_currency(app):
    currency_data = {"code": "CAD", "price": 1.25}

    with app.app_context():
        crud.create_currency(db, currency_data)
        crud.create_currency(db, currency_data)

    currencies = Currencies.query.all()
    assert len(currencies) == 1