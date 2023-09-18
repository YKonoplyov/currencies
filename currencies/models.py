from datetime import datetime

from currencies import db


class Currencies(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True, index=True)
    code = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_updated = db.Column(db.Date, default=datetime.now().date())
    __table_args__ = (
        db.UniqueConstraint(
            "code", "date_updated", "price",
            name="_code_date_updated_price_unique"
        ),
    )
