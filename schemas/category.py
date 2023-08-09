from marshmallow import Schema, fields

class CreateCategorySchema(Schema):
  name = fields.Str(required=True)
  parent = fields.Integer(missing=None)

class CategorySchema(Schema):
  class Meta:
    fields = ('id', 'name', 'parent_id', 'created_at', 'updated_at', 'deleted_at')