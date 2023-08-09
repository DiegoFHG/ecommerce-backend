from sqlalchemy.ext.associationproxy import association_proxy
from dataclasses import dataclass
from config import db
from datetime import datetime

class ProductCategory(db.Model):
  __tablename__ = 'product_category'

  product_id = db.Column(db.BigInteger, db.ForeignKey('products.id'), primary_key=True)
  category_id = db.Column(db.BigInteger, db.ForeignKey('categories.id'), primary_key=True)
  product = db.relationship('Product', back_populates='categories_association')
  category = db.relationship('Category', back_populates='products')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class ProductInventory(db.Model):
  __tablename__ = 'product_inventory'

  id = db.Column(db.BigInteger, primary_key=True)
  quantity = db.Column(db.Integer, nullable=False)
  product = db.Column(db.BigInteger, db.ForeignKey('products.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class Product(db.Model):
  __tablename__ = 'products'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, nullable=False)
  desc = db.Column(db.Text)
  price = db.Column(db.DECIMAL, nullable=False)
  currency_id = db.Column(db.BigInteger, db.ForeignKey('currencies.id'), nullable=False)
  tax_id = db.Column(db.BigInteger, db.ForeignKey('taxes.id'))
  discount_id = db.Column(db.BigInteger, db.ForeignKey('discounts.id'))
  active = db.Column(db.Boolean, default=False)
  img = db.Column(db.String)
  orders = db.relationship('OrderProducts', back_populates='product')
  categories_association = db.relationship('ProductCategory', back_populates='product')
  categories = association_proxy('categories_association', 'category')
  inventory = db.relationship('ProductInventory', backref='products', uselist=False, cascade="all, delete")
  carts = db.relationship('CartProduct', back_populates='product')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)