from dataclasses import dataclass

@dataclass
class ProductInventory():
  id: int
  quantity: int
  product: int

@dataclass
class Product():
  id: int
  name: str
  desc: str
  price: str
  currency: int
  tax: int
  discount: int
  active: bool
  inventory: ProductInventory