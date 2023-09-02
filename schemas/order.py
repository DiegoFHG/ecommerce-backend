from marshmallow import Schema, fields, validate
from .product import ProductSchema
from .currency import CurrencySchema

class CreateOrderSchema(Schema):
  cart = fields.Integer(required=True)
  line = fields.Str(required=True, validate=validate.Length(min=1))
  line_2 = fields.Str(validate=validate.Length(min=1))
  city = fields.Str(required=True)
  division = fields.Str(required=True)
  country = fields.Str(required=True)
  postal_code = fields.Str(required=True)
  recipient_name = fields.Str(required=True, validate=validate.Length(min=1))
  recipient_email = fields.Str(validate=validate.Email())
  recipient_phone_number = fields.Str(validate=validate.Length(max=20))
  shipping_type = fields.Integer(required=True)
  payment_type = fields.Integer(required=True)

class OrderStatus(Schema):
  id = fields.Integer()
  name = fields.Str()

class OrderDetails(Schema):
  id = fields.Integer()
  line = fields.Str()
  line2 = fields.Str()
  city = fields.Str()
  country = fields.Str()
  division = fields.Str()
  postal_code = fields.Str()
  recipient_name = fields.Str()
  recipient_email = fields.Str()
  recipient_phone_number = fields.Str()
  total = fields.Float()
  currency = fields.Nested(CurrencySchema)

class OrderSchema(Schema):
  id = fields.Integer()
  token = fields.Str()
  created_at = fields.Str()
  details = fields.Nested(OrderDetails)
  products = fields.List(fields.Nested(ProductSchema))
  status = fields.Nested(OrderStatus)