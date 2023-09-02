from random import choices
from string import ascii_letters, digits
from config import db
from models.orders import Order, OrderDetails, OrderProducts
from models.cart import Cart 

class OrderService():
  def get_all_orders(self):
    pass

  def get_order(self, id):
    order = db.get_or_404(Order, id)
    order_details = OrderDetails.query.filter_by(order=order.id).first()

    setattr(order, 'details', order_details)

    for i, product in enumerate(order.products):
      setattr(product, 'quantity', order.products_association[i].quantity)

    return order

  def create_order(self, order_info):
    cart = db.get_or_404(Cart, order_info['cart'])

    token = ''.join(choices(ascii_letters + digits, k=20))

    while Order.query.filter_by(token=token).first() is not None:
      token = ''.join(choices(ascii_letters + digits, k=20))
    
    order = Order(token=token) 

    db.session.add(order)
    db.session.commit()

    order_total = sum(p.price * p.quantity for p in cart.products)

    order_details = OrderDetails(
      order = order.id,
      line = f"{order_info['line']}, {order_info['line_2']}",
      city = order_info['city'],
      country = order_info['country'],
      division = order_info['division'],
      postal_code = order_info['postal_code'],
      recipient_name = order_info['recipient_name'],
      recipient_email = order_info['recipient_email'],
      recipient_phone_number = order_info['recipient_phone_number'],
      total = order_total,
      currency_id = cart.products[0].currency_id,
      shipping_type_id = order_info['shipping_type'],
      payment_type_id = order_info['payment_type']
    )

    db.session.add(order_details)
    db.session.commit()

    order_products = []

    for product in cart.products_association:
      order_products.append(OrderProducts(
        order_id = order.id,
        product_id = product.product_id,
        quantity = product.quantity
      ))

    db.session.add_all(order_products)
    db.session.commit()

    db.session.refresh(order_details)

    cart.products_association = []

    db.session.commit()

    return order_details
    