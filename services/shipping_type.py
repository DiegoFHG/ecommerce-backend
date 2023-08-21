from models.shipping_type import ShippingType

class ShippingTypeService():
  def get_all_shipping_types(self):
    shipping_types = ShippingType.query.all()

    return shipping_types