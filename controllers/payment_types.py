from flask import Blueprint, jsonify
from schemas.payment_type import PaymentTypeSchema
from services.payment_type import PaymentTypeService

payment_types = Blueprint('payment_types', __name__, url_prefix='/payment-types')
payment_type_service = PaymentTypeService()

@payment_types.get('/')
def get_all_payment_types():
  payment_types = payment_type_service.get_all_payment_types()
  payment_types = PaymentTypeSchema(many=True).dump(payment_types)

  return jsonify(payment_types)