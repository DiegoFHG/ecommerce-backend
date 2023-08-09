from config import db
from datetime import datetime

class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  products = db.relationship('ProductCategory', back_populates='category')
  parent_id = db.Column(db.BigInteger, db.ForeignKey('categories.id'))
  parents = db.relationship('Category', remote_side=[id])
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)