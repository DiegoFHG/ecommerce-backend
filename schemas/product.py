from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from models.product import Product
from .currency import CurrencySchema
from .tax import TaxSchema
from .discount import DiscountSchema
from .category import CategorySchema

class CreateProductSchema(Schema):
  name = fields.Str(required=True)
  desc = fields.Str(required=True)
  price = fields.Decimal(required=True)
  currency = fields.Integer(required=True)
  tax = fields.Integer(required=True)
  discount = fields.Integer(required=True)
  quantity = fields.Integer(required=True)
  categories = fields.List(fields.Integer)

class ProductSchema(SQLAlchemySchema):
  class Meta:
    model = Product
    include_relationships = True
    include_fk = True
    fields = (
      'id',
      'name',
      'desc',
      'price',
      'currency',
      'tax',
      'discount',
      'created_at',
      'updated_at',
      'img',
      'quantity',
      'categories',
      'created_at',
      'updated_at'
    )

  id = auto_field()
  name = auto_field()
  desc = auto_field()
  price = fields.Float()
  currency = Nested(CurrencySchema)
  tax = Nested(TaxSchema)
  discount = Nested(DiscountSchema)
  categories = Nested(CategorySchema, many=True)
  img = auto_field()
  created_at = auto_field()
  updated_at = auto_field()