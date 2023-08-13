from flask import Blueprint, jsonify, request
from schemas.product import ProductSchema, CreateProductSchema
from services.product import ProductService

products = Blueprint('products', __name__, url_prefix='/products')

product_service = ProductService()

@products.get('/')
def index():
  url_params = request.args
  page = int(url_params.get('page', 0))
  limit = int(url_params.get('limit', 10))

  products, count = product_service.get_all_products(page, limit)

  products = ProductSchema(many=True).dump(products)

  return jsonify({ 'products': products, 'total': count })

@products.get('/<id>')
def get(id):
  found_product = product_service.get_product(id)
  found_product = ProductSchema().dump(found_product)

  return jsonify(found_product)

@products.post('/')
def create():
  errors = CreateProductSchema().validate(request.json)

  if errors:
    return errors, 400

  product_info = CreateProductSchema().dump(request.json)

  new_product = product_service.create_product(product_info=product_info)
  new_product = ProductSchema().dump(new_product)

  return jsonify(new_product)

@products.put('/<id>')
def update(id):
  return jsonify({ 'msg': 'To implement' })

@products.delete('/<id>')
def delete(id):
  deleted_product = product_service.delete_product(id)

  if deleted_product == True:
    return jsonify({ 'msg': f'product with ID {id} deleted' })
  else:
    return jsonify({ 'msg': f'product with ID {id} not found' }), 404