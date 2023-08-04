from flask import Flask
from controllers import products, categories

app = Flask('ecommerce')

app.register_blueprint(products.products)
app.register_blueprint(categories.categories)

if __name__ == '__main__':
    app.run()