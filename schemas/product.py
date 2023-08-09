from marshmallow import Schema, fields
from schemas import currency, tax, discount, category

class CreateProductSchema(Schema):
  name = fields.Str(required=True)
  desc = fields.Str(required=True)
  price = fields.Decimal(required=True)
  currency = fields.Integer(required=True)
  tax = fields.Integer(required=True)
  discount = fields.Integer(required=True)
  quantity = fields.Integer(required=True)
  categories = fields.List(fields.Integer)

class ProductSchema(Schema):
  price = fields.Float()
  class Meta:
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
      'categories'
    )

  currency = fields.Nested(currency.CurrencySchema)
  tax = fields.Nested(tax.TaxSchema)
  discount = fields.Nested(discount.DiscountSchema)
  categories = fields.List(fields.Nested(category.CategorySchema))