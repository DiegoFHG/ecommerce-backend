from config import app
from controllers import products, categories, users, carts, payment_types, shipping_types, orders

app.register_blueprint(products.products)
app.register_blueprint(categories.categories)
app.register_blueprint(users.users)
app.register_blueprint(carts.carts)
app.register_blueprint(payment_types.payment_types)
app.register_blueprint(shipping_types.shipping_types)
app.register_blueprint(orders.orders)

if __name__ == '__main__':
    app.run()