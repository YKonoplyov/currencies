from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from currencies.config import Config
from scheduler import scheduler

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_type: Config) -> APIFlask:
    app = APIFlask(__name__)
    app.config.from_object(config_type)

    db.init_app(app)
    ma.init_app(app)

    scheduler.api_enabled = True
    scheduler.init_app(app)
    return app
