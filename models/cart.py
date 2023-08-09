from config import db
from datetime import datetime

class CartProduct(db.Model):
  __tablename__ = 'cart_products'

  cart_id = db.Column(db.BigInteger, db.ForeignKey('shopping_carts.id'), primary_key=True)
  product_id = db.Column(db.BigInteger, db.ForeignKey('products.id'), primary_key=True)
  quantity = db.Column(db.Integer)
  cart = db.relationship('Cart', back_populates='products')
  product = db.relationship('Product', back_populates='carts')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class Cart(db.Model):
  __tablename__ = 'shopping_carts'

  id = db.Column(db.BigInteger, primary_key=True)
  # user = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=True)
  token = db.Column(db.String, unique=True, nullable=True)
  products = db.relationship('CartProduct', back_populates='cart')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)