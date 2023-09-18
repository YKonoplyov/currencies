import os

from dotenv import load_dotenv
from requests import request

load_dotenv()


def get_all_exchange_value() -> dict[str, float]:
    url = (
        f"https://v6.exchangerate-api.com/v6/{os.getenv('API_KEY')}/latest/USD"
    )
    response = request("GET", url)
    data = response.json()
    return data.get("conversion_rates")


def get_currencies_value(currencies_codes: list[str]) -> dict:
    exchange_rates = get_all_exchange_value()
    currencies_rates = {}
    for code in currencies_codes:
        currencies_rates[code] = exchange_rates.get(code)

    return currencies_rates
