from marshmallow import Schema

class DiscountSchema(Schema):
  class Meta:
    fields = ('id', 'name', 'percentage')