from marshmallow import Schema, fields

class TaxSchema(Schema):
  class Meta:
    fields = ('id', 'name', 'percentage')

  percentage = fields.Float()