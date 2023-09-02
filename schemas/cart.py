from marshmallow import Schema, fields
from .product import ProductSchema

class AddProductToTokenCartSchema(Schema):
  product = fields.Integer(required=True, strict=True, validate=lambda x: x > 0)  
  quantity = fields.Integer(required=True, strict=True, validate=lambda x: x > 0)

class CartSchema(Schema):
  class Meta:
    fields = ('token', 'products', 'id')
  
  products = fields.List(fields.Nested(ProductSchema))