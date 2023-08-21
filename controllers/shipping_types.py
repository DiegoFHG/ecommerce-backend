from flask import Blueprint, jsonify
from schemas.shipping_type import ShippingTypeSchema
from services.shipping_type import ShippingTypeService

shipping_types = Blueprint('shipping_types', __name__, url_prefix='/shipping-types')
shipping_type_service = ShippingTypeService()

@shipping_types.get('/')
def get_all_shipping_types():
  shipping_types = shipping_type_service.get_all_shipping_types()
  shipping_types = ShippingTypeSchema(many=True).dump(shipping_types)

  return jsonify(shipping_types)