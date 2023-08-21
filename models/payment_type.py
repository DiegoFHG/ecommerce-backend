from config import db
from datetime import datetime

class PaymentType(db.Model):
    __tablename__ = 'payment_types'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    # order_details = db.relationship('OrderDetails', backref='payment_type')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) 
    deleted_at = db.Column(db.DateTime)