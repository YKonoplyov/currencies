from psycopg2.errors import UniqueViolation


from constants import CURRENCIES_TO_SAVE
from currencies import exchange_api_requests, crud, db, create_app, scheduler
from currencies.config import develop

app = create_app(develop)

scheduler.remove_all_jobs()


@scheduler.scheduler.scheduled_job(
    id="get_currencies",
    trigger="cron",
    hour=2,
)
def get_main_currencies():
    currencies_values = exchange_api_requests.get_currencies_value(
        CURRENCIES_TO_SAVE
    )
    for code, price in currencies_values.items():
        with app.app_context():
            crud.create_currency(
                db=db, currency_data={"code": code, "price": price}
            )
            print(code, price)
