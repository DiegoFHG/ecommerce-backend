from config import db
from datetime import datetime

class OrderProducts(db.Model):
  __tablename__ = 'order_products'

  order = db.Column(db.BigInteger, db.ForeignKey('orders.id'), primary_key=True)
  product = db.Column(db.BigInteger, db.ForeignKey('products.id'), primary_key=True)
  quantity = db.Column(db.Integer)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class OrderDetails(db.Model):
  __tablename__ = 'order_details'

  id = db.Column(db.BigInteger, primary_key=True)
  line = db.Column(db.String, nullable=False)
  city = db.Column(db.String, nullable=False)
  country = db.Column(db.String, nullable=False)
  postal_code = db.Column(db.String, nullable=False)
  recipient_name = db.Column(db.String, nullable=False)
  recipient_last_name = db.Column(db.String, nullable=False)
  total = db.Column(db.DECIMAL, nullable=False)
  currency = db.Column(db.BigInteger, nullable=False)
  shipping_type = db.Column(db.BigInteger, db.ForeignKey('shipping_types.id'), nullable=False)
  payment_type = db.Column(db.BigInteger, db.ForeignKey('payment_types.id'), nullable=False)
  orders = db.relationship('Order', back_populates='order_details', uselist=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)

class Order(db.Model):
  __tablename__ = 'orders'

  id = db.Column(db.BigInteger, primary_key=True)
  details = db.Column(db.BigInteger, db.ForeignKey('order_details.id'))
  products = db.relationship('Product', secondary=OrderProducts, back_populates='orders')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)