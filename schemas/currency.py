from marshmallow import Schema, fields

class CurrencySchema(Schema):
  class Meta:
    fields = ('id', 'name', 'symbol', 'percentage')

  percentage = fields.Float()