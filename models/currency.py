from config import db
from datetime import datetime

class Currency(db.Model):
  __tablename__ = 'currencies'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  symbol = db.Column(db.String, unique=True, nullable=False)
  products = db.relationship('Product', backref='currency')
  order_details = db.relationship('OrderDetails', backref='currency')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)