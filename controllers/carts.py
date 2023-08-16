from flask import Blueprint, jsonify, request, abort
from services.cart import CartService
from schemas import cart

carts = Blueprint('carts', __name__, url_prefix='/carts')
cart_service = CartService()

@carts.get('/<token>')
def get_by_token(token):
  token_cart = cart_service.get_token_cart(token)

  if token_cart is None:
    return abort(404)

  token_cart = cart.CartSchema().dump(token_cart)

  return jsonify(token_cart)

@carts.get('/<token>/clear')
def clear_cart_by_token(token):
  clear_cart = cart_service.clear_token_cart(token)

  if clear_cart is None:
    return abort(404)

  clear_cart = cart.CartSchema().dump(clear_cart)

  return jsonify(clear_cart)

@carts.post('/')
def create_token_cart():
  new_cart = cart_service.create_token_cart()
  new_cart = cart.CartSchema().dump(new_cart)

  return jsonify(new_cart)

@carts.post('/<token>/products')
def add_product_to_token_cart(token):
  errors = cart.AddProductToTokenCartSchema().validate(request.json)

  if errors:
    return errors, 400

  cart_product = cart.AddProductToTokenCartSchema().dump(request.json)

  added_product = cart_service.add_product_to_token_cart(token, cart_product)
  added_product = cart.CartSchema().dump(added_product)

  return jsonify(added_product)

@carts.post('/<token>/products/quantity')
def change_product_quantity_token_cart(token):
  errors = cart.AddProductToTokenCartSchema().validate(request.json)

  if errors:
    return errors, 400

  cart_product = cart.AddProductToTokenCartSchema().dump(request.json)

  new_cart = cart_service.change_product_quantity_from_token_cart(token, cart_product)

  if new_cart is None:
    return abort(404)
  
  new_cart = cart.CartSchema().dump(new_cart)

  return jsonify(new_cart)