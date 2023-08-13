from flask import Blueprint, jsonify, request
from schemas.category import CategorySchema, CreateCategorySchema
from schemas.product import ProductSchema
from services.category import CategoryService
from services.product import ProductService

categories = Blueprint('categories', __name__, url_prefix='/categories')
category_service = CategoryService()
product_service = ProductService()

@categories.get('/')
def index():
  categories = category_service.get_all_categories(parents_only=False)
  categories = CategorySchema(many=True).dump(categories)

  return jsonify(categories)

@categories.get('/<id>')
def get(id):
  found_category = category_service.get_category(id)
  found_category = CategorySchema().dump(found_category)

  return jsonify(found_category)

@categories.get('/<id>/products')
def get_(id):
  url_params = request.args
  page = int(url_params.get('page', 0))
  limit = int(url_params.get('limit', 10))

  products, count = product_service.get_by_category(id, page, limit)
  products = ProductSchema(many=True).dump(products)

  print(products)

  return jsonify({ 'products': products, 'total': count })

@categories.get('/<id>/subcategories')
def get_category_subcategories(id):
  subcategories = category_service.get_category_subcategories(id)
  subcategories = CategorySchema(many=True).dump(subcategories)

  return jsonify(subcategories)

@categories.get('/<id>/tree')
def get_category_tree(id):
  tree = category_service.get_category_tree(id)
  tree = CategorySchema(many=True).dump(tree)

  return jsonify(tree)

@categories.post('/')
def create():
  errors = CreateCategorySchema().validate(request.json)

  if errors:
    return errors, 400

  category_info = CreateCategorySchema().dump(request.json)

  new_category = category_service.create_category(category_info=category_info)
  new_category = CategorySchema().dump(new_category)

  return jsonify(new_category)

@categories.put('/<id>')
def update(id):
  return jsonify({ 'msg': 'To implement' })

@categories.delete('/<id>')
def delete(id):
  return jsonify({ 'msg': 'To implement' })