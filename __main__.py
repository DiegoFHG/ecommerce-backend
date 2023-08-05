from flask import Flask
from controllers import products, categories, users

app = Flask('ecommerce')

app.register_blueprint(products.products)
app.register_blueprint(categories.categories)
app.register_blueprint(users.users)

if __name__ == '__main__':
    app.run()