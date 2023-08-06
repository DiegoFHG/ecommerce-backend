from config import db
from datetime import datetime

class ShippingType(db.Model):
    __tablename__ = 'shipping_types'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    order_details = db.relationship('OrderDetails', back_populates='shipping_types')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
    deleted_at = db.Column(db.DateTime)