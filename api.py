from flask import Flask, send_file
from flask_cors import CORS
from flask_restful import Resource, Api


class Products(Resource):
    def get(self):
        return "Products"


class Product_Details(Resource):
    def get(self, product_id):
        return "A Product"


app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(Products, '/products')
api.add_resource(Product_Details, '/products/<product_id>')

if __name__ == '__main__':
    app.run(port=5002)
