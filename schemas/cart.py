from marshmallow import Schema, fields

class AddProductToTokenCartSchema(Schema):
  product = fields.Integer(required=True)
  quantity = fields.Integer(required=True)