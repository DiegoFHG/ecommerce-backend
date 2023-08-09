from marshmallow import Schema, fields
from schemas import product

class AddProductToTokenCartSchema(Schema):
  product = fields.Integer(required=True)
  quantity = fields.Integer(required=True)

class CartSchema(Schema):
  class Meta:
    fields = ('token', 'products')
  
  products = fields.List(fields.Nested(product.ProductSchema))