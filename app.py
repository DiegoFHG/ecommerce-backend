from config import app
from controllers import products, categories, users, carts

app.register_blueprint(products.products)
app.register_blueprint(categories.categories)
app.register_blueprint(users.users)
app.register_blueprint(carts.carts)

if __name__ == '__main__':
    app.run()