from config import db
from datetime import datetime

class Discount(db.Model):
  __tablename__ = 'discounts'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  percentage = db.Column(db.DECIMAL, nullable=False)
  products = db.relationship('Product', backref='discount')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)