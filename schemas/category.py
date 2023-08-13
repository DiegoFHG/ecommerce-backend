from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import category

class CreateCategorySchema(Schema):
  name = fields.Str(required=True)
  parent = fields.Integer(missing=None)

class CategorySchema(SQLAlchemySchema):
  class Meta:
    model = category.Category
    include_relationships = True
    include_fk = True
    fields = ('id', 'name', 'parent_id', 'created_at', 'updated_at')

  id = auto_field()
  name = auto_field()
  parent_id = auto_field()
  created_at = auto_field()
  updated_at = auto_field()
