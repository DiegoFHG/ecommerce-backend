from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.orders import OrderDetails

class CreateOrderSchema(Schema):
  cart = fields.Integer(required=True)
  line = fields.Str(required=True)
  line_2 = fields.Str()
  city = fields.Str(required=True)
  division = fields.Str(required=True)
  country = fields.Str(required=True)
  postal_code = fields.Str(required=True)
  recipient_name = fields.Str(required=True)
  recipient_email = fields.Str()
  recipient_phone_number = fields.Str()
  shipping_type = fields.Integer(required=True)
  payment_type = fields.Integer(required=True)

class OrderSchema(SQLAlchemySchema):
  class Meta:
    model = OrderDetails
    include_relationships = True
    fields = (
      'order',
      'line',
      'city',
      'country',
      'division',
      'postal_code',
      'recipient_name',
      'recipient_email',
      'recipient_phone_number',
      'total',
      'created_at'
    )

  order = auto_field(data_key='id')
  line = auto_field()
  city = auto_field()
  country = auto_field()
  division = auto_field()
  postal_code = auto_field()
  recipient_name = auto_field()
  recipient_email = auto_field()
  recipient_phone_number = auto_field()
  total = fields.Float()
  created_at = auto_field()
  # products = auto_field()