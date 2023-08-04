from flask import Blueprint, jsonify

users = Blueprint('users', __name__, url_prefix='/users')

@users.get('/')
def index():
    return jsonify({ 'msg': 'Hello world from users'})

@users.get('/<id>')
def get(id):
  return jsonify({ 'msg': 'id is', 'id': id })

@users.post('/')
def create():
  return jsonify({ 'msg': 'To implement' })

@users.put('/<id>')
def update(id):
   return jsonify({ 'msg': 'To implement' })

@users.delete('/<id>')
def delete(id):
   return jsonify({ 'msg': 'To implement' })