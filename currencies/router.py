from datetime import datetime
from apiflask import APIBlueprint

from currencies import crud, exchange_api_requests, schemas
from currencies.models import Currencies
from constants import CURRENCIES_TO_SAVE
from currencies import db

currency_blueprint = APIBlueprint(
    "urls",
    __name__,
)


@currency_blueprint.get(
    "/currencies/history",
)
@currency_blueprint.input(schemas.CurrencyFilterArgs, location="query")
@currency_blueprint.output(schemas.Currency(many=True))
def get_currencies_history(query_data):
    print(query_data)
    date_from = query_data.get("date_from")
    currency_code = query_data.get("currency_code")
    currencies = crud.get_currencies_list()
    if date_from:
        currencies = currencies.filter(Currencies.date_updated >= date_from)
    if currency_code:
        currencies = currencies.filter(Currencies.code == currency_code)
    return currencies


@currency_blueprint.get("/currencies/<currency_code>")
@currency_blueprint.output(schema=schemas.CurrencyRead)
def get_curency_value(currency_code):
    currencies_prices = exchange_api_requests.get_currencies_value([currency_code])
    if currency_code in CURRENCIES_TO_SAVE:
        crud.create_currency(
            db=db,
            currency_data={
                "code": currency_code,
                "price": currencies_prices.get(currency_code),
            },
        )
    currency = Currencies(
        code=currency_code,
        price=currencies_prices.get(currency_code),
        date_updated=datetime.now().date(),
    )
    return currency
