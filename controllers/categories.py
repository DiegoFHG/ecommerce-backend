from flask import Blueprint, jsonify, request
from schemas import category
from services.category import CategoryService

categories = Blueprint('categories', __name__, url_prefix='/categories')
category_service = CategoryService()

@categories.get('/')
def index():
  return jsonify({ 'msg': 'Hello world from categories'})

@categories.get('/<id>')
def get(id):
  found_category = category_service.get_category(id)
  found_category = category.CategorySchema().dump(found_category)

  return jsonify(found_category)

@categories.get('/<id>/subcategories')
def get_category_subcategories(id):
  subcategories = category_service.get_category_subcategories(id)
  subcategories = category.CategorySchema(many=True).dump(subcategories)

  return jsonify(subcategories)

@categories.get('/<id>/tree')
def get_category_tree(id):
  tree = category_service.get_category_tree(id)
  tree = category.CategorySchema(many=True).dump(tree)

  return jsonify(tree)

@categories.post('/')
def create():
  errors = category.CreateCategorySchema().validate(request.json)

  if errors:
    return errors, 400

  category_info = category.CreateCategorySchema().dump(request.json)

  new_category = category_service.create_category(category_info=category_info)
  new_category = category.CategorySchema().dump(new_category)

  return jsonify(new_category)

@categories.put('/<id>')
def update(id):
  return jsonify({ 'msg': 'To implement' })

@categories.delete('/<id>')
def delete(id):
  return jsonify({ 'msg': 'To implement' })