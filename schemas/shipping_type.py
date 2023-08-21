from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.shipping_type import ShippingType

class ShippingTypeSchema(SQLAlchemySchema):
  class Meta:
    model = ShippingType
    fields = (
      'id', 'name'
    )
  
  id = auto_field()
  name = auto_field()