from dataclasses import dataclass
from decimal import Decimal

@dataclass
class OrderDetails():
  id: int
  order: int
  line: str
  city: str
  country: str
  recipient_name: str
  recipient_last_name: str
  total: Decimal
  currency: int
  shipping_type: int
  payment_type: int

@dataclass
class Order():
  id: int
  details: OrderDetails