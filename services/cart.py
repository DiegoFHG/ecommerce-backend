from random import choices
from string import ascii_letters, digits
from config import db
from models.cart import Cart, CartProduct
from models.product import Product

class CartService():
  def get_token_cart(self, token):
    cart = Cart.query.filter_by(token=token).first()

    for i, product in enumerate(cart.products):
      setattr(product, 'quantity', cart.products_association[i].quantity)

    return cart

  def create_token_cart(self):
    token = ''.join(choices(ascii_letters + digits, k=20))

    while Cart.query.filter_by(token=token).first() is not None:
      token = ''.join(choices(ascii_letters + digits, k=20))

    cart = Cart(
      token=token
    )

    db.session.add(cart)
    db.session.commit()
    db.session.refresh(cart)

    return cart

  def clear_token_cart(self, token):
    cart = Cart.query.filter_by(token=token).first()

    if cart is None:
      return None

    CartProduct.query.filter_by(cart_id=cart.id).delete()

    db.session.commit()

    for i, product in enumerate(cart.products):
      setattr(product, 'quantity', cart.products_association[i].quantity)

    return cart

  def add_product_to_token_cart(self, token, cart_product_info):
    cart = Cart.query.filter_by(token=token).first()
    product = Product.query.filter_by(id=cart_product_info['product']).first()

    if cart is None or product is None:
      return None

    found_cart_product = CartProduct.query.filter_by(cart_id=cart.id, product_id=cart_product_info['product']).first()

    if found_cart_product:
      return False

    cart_product = CartProduct(
      cart_id = cart.id,
      product_id = cart_product_info['product'],
      quantity = product.inventory.quantity if cart_product_info['quantity'] > product.inventory.quantity else cart_product_info['quantity']
    )

    db.session.add(cart_product)
    db.session.commit()
    db.session.refresh(cart)

    for i, product in enumerate(cart.products):
      setattr(product, 'quantity', cart.products_association[i].quantity)

    return cart

  def change_product_quantity_from_token_cart(self, token, cart_product_info):
    cart = Cart.query.filter_by(token=token).first()

    if cart is None:
      return None

    cart_product = CartProduct.query.filter_by(cart_id=cart.id, product_id=cart_product_info['product']).first()

    print(cart_product)

    if cart_product is None:
      return None

    if cart_product_info['quantity'] == 0:
      db.session.delete(cart_product)
      db.session.commit()
      db.session.refresh(cart)

    else:
      cart_product.quantity = cart_product_info['quantity']

      db.session.commit()
      db.session.refresh(cart)

    for i, product in enumerate(cart.products):
      setattr(product, 'quantity', cart.products_association[i].quantity)

    return cart