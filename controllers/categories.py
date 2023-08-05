from flask import Blueprint, jsonify

categories = Blueprint('categories', __name__, url_prefix='/categories')

@categories.get('/')
def index():
  return jsonify({ 'msg': 'Hello world from categories'})

@categories.get('/<id>')
def get(id):
  return jsonify({ 'msg': 'id is', 'id': id })

@categories.post('/')
def create():
  return jsonify({ 'msg': 'To implement' })

@categories.put('/<id>')
def update(id):
  return jsonify({ 'msg': 'To implement' })

@categories.delete('/<id>')
def delete(id):
  return jsonify({ 'msg': 'To implement' })