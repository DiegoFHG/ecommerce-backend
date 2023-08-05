from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Discount():
  id: int
  name: str
  percentage: Decimal