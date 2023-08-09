from marshmallow import Schema

class TaxSchema(Schema):
  class Meta:
    fields = ('id', 'name', 'percentage')