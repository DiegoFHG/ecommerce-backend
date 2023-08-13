from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from datetime import datetime

class Category(db.Model):
  __tablename__ = 'categories'

  id = db.Column(db.BigInteger, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  product_association = db.relationship('ProductCategory', back_populates='category')
  products = association_proxy('product_association', 'product')
  parent_id = db.Column(db.BigInteger, db.ForeignKey('categories.id'))
  parents = db.relationship('Category', remote_side=[id])
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
  deleted_at = db.Column(db.DateTime)