from sqlalchemy.orm import selectinload
from config import db
from models.product import Product, ProductInventory
from models.currency import Currency

class ProductService():
  def get_all_products(self, page, limit):
    products = None
    count = Product.query.count()

    if (page != 0):
      products = Product.query.paginate(page=page, per_page=limit)
    else:
      products = Product.query.all() 

    return products, count

  def get_product(self, id):
    product = db.get_or_404(Product, id)
    product.quantity = product.inventory.quantity

    return product

  def get_by_category(self, category, page, limit):
    products = None
    count = Product.query.filter(Product.categories.any(id=category)).count()

    if (page != 0):
      products = Product.query.join(Currency).filter(Product.categories.any(id=category)).paginate(page=page, per_page=limit)
    else:
      products = Product.query.options(selectinload(Product.inventory).load_only(ProductInventory.quantity)).filter(Product.categories.any(id=category)).all()

    for product in products:
      product.quantity = product.inventory.quantity

    return products, count

  def create_product(self, product_info):
    product = Product(
      name=product_info['name'],
      desc=product_info['desc'],
      price=product_info['price'],
      currency_id=product_info['currency'],
      tax_id=product_info['tax'],
      discount_id=product_info['discount']
    )

    db.session.add(product)
    db.session.commit()

    product_inventory = ProductInventory(quantity=product_info['quantity'], product=product.id)

    db.session.add(product_inventory)
    db.session.commit()

    db.session.refresh(product)

    return product

  def delete_product(self, id):
    try:
      product = db.session.execute(db.select(Product).filter_by(id=id)).scalar_one()

      db.session.delete(product)
      db.session.commit()

      return True
    except:
      return False