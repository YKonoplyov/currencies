from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from currencies.models import Currencies


def get_currencies_list():
    return Currencies.query


def create_currency(db: SQLAlchemy, currency_data: dict):
    currency = Currencies(**currency_data)
    try:
        db.session.add(currency)
        db.session.commit()
    except IntegrityError:
        pass
    return currency
