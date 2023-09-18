from currencies import ma
from currencies.models import Currencies
from marshmallow import fields


class CurrencyBase(ma.SQLAlchemySchema):
    class Meta:
        model = Currencies

    code = ma.auto_field()
    price = ma.auto_field()


class CurrencyCreate(CurrencyBase):
    pass


class Currency(CurrencyBase):
    id = ma.auto_field()
    date_updated = ma.auto_field()


class CurrencyRead(CurrencyBase):
    date_updated = ma.auto_field()


class CurrencyFilterArgs(ma.Schema):
    date_from = fields.Str()
    currency_code = fields.Str()
