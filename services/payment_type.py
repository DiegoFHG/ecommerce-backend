from models.payment_type import PaymentType

class PaymentTypeService():
  def get_all_payment_types(self):
    payment_types = PaymentType.query.all()

    return payment_types