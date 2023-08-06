from config import app
from controllers import products, categories, users
from models import category, currency, discount, orders, payment_type, product, shipping_type, tax

app.register_blueprint(products.products)
app.register_blueprint(categories.categories)
app.register_blueprint(users.users)

if __name__ == '__main__':
    app.run()