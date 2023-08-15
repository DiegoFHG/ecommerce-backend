from marshmallow import Schema, fields

class DiscountSchema(Schema):
  class Meta:
    fields = ('id', 'name', 'percentage')

  percentage = fields.Float()