from marshmallow import Schema

class CurrencySchema(Schema):
  class Meta:
    fields = ('id', 'name', 'symbol', 'percentage')