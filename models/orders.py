from config import db
from datetime import datetime

class OrderProducts(db.Model):
  __tablename__ = 'order_products'

  order_id = db.Column(db.BigInteger, db.ForeignKey('orders.id'), primary_key=True)
  product_id = db.Column(db.BigInteger, db.ForeignKey('products.id'), primary_key=True)
  quantity = db.Column(db.Integer)
  order = db.relationship('Order', back_populates='products')
  product = db.relationship('Product', back_populates='orders')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class OrderDetails(db.Model):
  __tablename__ = 'order_details'

  id = db.Column(db.BigInteger, primary_key=True)
  order = db.Column(db.BigInteger, db.ForeignKey('orders.id'))
  line = db.Column(db.String, nullable=False)
  city = db.Column(db.String, nullable=False)
  country = db.Column(db.String, nullable=False)
  division = db.Column(db.String, nullable=False)
  postal_code = db.Column(db.String, nullable=False)
  recipient_name = db.Column(db.String, nullable=False)
  recipient_email = db.Column(db.String)
  recipient_phone_number = db.Column(db.String)
  # user_id = db.Column(db.BigInteger)
  # user = db.relationship('User')
  total = db.Column(db.DECIMAL, nullable=False)
  currency_id = db.Column(db.BigInteger, db.ForeignKey('currencies.id'), nullable=False)
  shipping_type_id = db.Column(db.BigInteger, db.ForeignKey('shipping_types.id'), nullable=False)
  payment_type_id = db.Column(db.BigInteger, db.ForeignKey('payment_types.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class Order(db.Model):
  __tablename__ = 'orders'

  id = db.Column(db.BigInteger, primary_key=True)
  token = db.Column(db.String, unique=True, nullable=True)
  details = db.relationship('OrderDetails', backref='orders', uselist=False)
  products = db.relationship('OrderProducts', back_populates='order')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)