from config import db
from datetime import datetime

class Tax(db.Model):
  __tablename__ = 'taxes'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  percentage = db.Column(db.DECIMAL, nullable=False)
  products = db.relationship('Product', backref='tax')
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)