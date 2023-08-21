from flask import Blueprint, jsonify, request
from services.order import OrderService
from schemas.order import CreateOrderSchema, OrderSchema

orders = Blueprint('orders', __name__, url_prefix='/orders')
order_service = OrderService()

@orders.get('/')
def index():
  pass

@orders.post('/')
def create():
  errors = CreateOrderSchema().validate(request.json)

  if errors:
    return errors, 400

  order_info = CreateOrderSchema().dump(request.json)

  new_order = order_service.create_order(order_info)
  new_order = OrderSchema().dump(new_order)

  return jsonify(new_order)