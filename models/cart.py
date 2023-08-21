from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from config import db

class CartProduct(db.Model):
  __tablename__ = 'cart_products'

  id = db.Column(db.BigInteger, primary_key=True)
  cart_id = db.Column(db.BigInteger, db.ForeignKey('shopping_carts.id'))
  product_id = db.Column(db.BigInteger, db.ForeignKey('products.id'))
  quantity = db.Column(db.Integer)
  cart = db.relationship('Cart', back_populates='products_association')
  product = db.relationship('Product', back_populates='carts')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class Cart(db.Model):
  __tablename__ = 'shopping_carts'

  id = db.Column(db.BigInteger, primary_key=True)
  # user = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=True)
  token = db.Column(db.String, unique=True, nullable=True)
  products_association = db.relationship('CartProduct', back_populates='cart', cascade='all, delete-orphan')
  products = association_proxy('products_association', 'product')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)