from flask import Blueprint, jsonify
from schemas import product

products = Blueprint('products', __name__, url_prefix='/products')

@products.get('/')
def index():
  product.ProductSchema().validate
  return jsonify({ 'msg': 'Hello world from products'})

@products.get('/<id>')
def get(id):
  return jsonify({ 'msg': 'id is', 'id': id })

@products.post('/')
def create():
  return jsonify({ 'msg': 'To implement' })

@products.put('/<id>')
def update(id):
  return jsonify({ 'msg': 'To implement' })

@products.delete('/<id>')
def delete(id):
  return jsonify({ 'msg': 'To implement' })