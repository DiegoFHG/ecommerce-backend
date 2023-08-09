from flask import Blueprint, jsonify, request
from services.cart import CartService
from schemas import cart

carts = Blueprint('carts', __name__, url_prefix='/carts')
cart_service = CartService()

@carts.get('/<token>')
def get_by_token(token):
  pass

@carts.get('/<token>/clear')
def clear_cart_by_token(token):
  pass

@carts.post('/<token>/products')
def add_product_to_token_cart(token):
  errors = cart.AddProductToTokenCartSchema().validate(request.json)

  if errors:
    return errors, 400

  cart_product = cart.AddProductToTokenCartSchema().dump(request.json)

  added_product = cart_service.add_product_to_token_cart(token, cart_product)
  added_product = cart.TokenCartProductSchema().dump(added_product)

  return jsonify(added_product)