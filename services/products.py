from config import db
from models.product import Product, ProductInventory
from schemas.product import CreateProductSchema

class ProductService():
  def get_all_products(self, page, limit):
    products = None
    count = Product.query.count()

    if (page != 0):
      products = Product.query.paginate(page=page, per_page=limit)

      return products, count

    products = Product.query.all()
    
    return products, count

  def get_product(self, id):
    return db.get_or_404(Product, id)

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