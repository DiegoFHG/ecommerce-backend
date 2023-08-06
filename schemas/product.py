from marshmallow import Schema, fields

class ProductSchema(Schema):
  name = fields.Str()
  desc = fields.Str()
  price = fields.Decimal()
  currency = fields.Integer()
  tax = fields.Integer()
  discount = fields.Integer()