import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from dotenv import load_dotenv
from flask_migrate import Migrate


from currencies import create_app, db
from currencies.config import develop
from currencies.router import currency_blueprint
from scheduler.tasks import scheduler

load_dotenv()

app = create_app(develop)
app.register_blueprint(currency_blueprint, url_prefix="/api/v1")
scheduler.scheduler.add_jobstore(
    jobstore=SQLAlchemyJobStore(url=os.getenv("POSTGRES_URL"))
)
migrate = Migrate(app, db)


if __name__ == "__main__":
    scheduler.start()
    app.run(debug=True)
