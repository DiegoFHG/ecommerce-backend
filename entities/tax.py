from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Tax():
  id: int
  name: str
  percentage: Decimal