from config import db
from datetime import datetime
from models.orders import OrderProducts

class ProductCategory(db.Model):
  __tablename__ = 'product_category'

  product = db.Column(db.BigInteger, db.ForeignKey('products.id'), primary_key=True)
  category = db.Column(db.BigInteger, db.ForeignKey('categories.id'), primary_key=True)
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
  currency = db.Column(db.BigInteger, db.ForeignKey('currencies.id'), nullable=False)
  tax = db.Column(db.BigInteger, db.ForeignKey('taxes.id'))
  discount = db.Column(db.BigInteger, db.ForeignKey('discounts.id'))
  active = db.Column(db.Boolean, default=False)
  orders = db.relationship('Order', secondary=OrderProducts, back_populates='products')
  inventory = db.relationship('ProductInventory', back_populates='products', uselist=False)
  categories = db.relationship('Categories', secondary=ProductCategory, back_populates='products')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)