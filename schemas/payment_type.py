from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models.payment_type import PaymentType

class PaymentTypeSchema(SQLAlchemySchema):
  class Meta:
    model = PaymentType
    fields = (
      'id', 'name'
    )
  
  id = auto_field()
  name = auto_field()