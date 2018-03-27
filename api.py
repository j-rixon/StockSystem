from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Resource, Api
from dbCtrl import dbCtrl


class Products(Resource): # contains all functions for the main screen
    def get(self):  # the read function
        return jsonify(db.filterQuery().fetchall())   #return a JSON dict of everything (filterQuery() without parameters)

    def post(self):
        json_data = request.get_json(force=True)    # get the json data that is passed to it
        Id = json_data['ID']    # assign variables from the JSON
        category = json_data['Category']
        name = json_data['Name']
        qty = json_data['Quantity']  # these cannot be anything but numbers due to the type of input used, no validation needed
        price = json_data['Price']   #
        extrainfo = json_data['extrainfo']
        db.createItem(sqlClean(Id), sqlClean(name), sqlClean(category), price, qty, sqlClean(extrainfo)) # create or update the entry using 'cleaned' values


class Product(Resource): # what is called when referring to a specific product (i.e. dealing with a specific item)
    def delete(self, productid):  # productid is pulled from the URL as shown below in the add_resource statement
        db.deleteItem(productid)  # delete the item using the database module


class Search(Resource):
    def post(self):
        json_data = request.get_json(force=True)    # get the json data that is passed to it
        Id = valueOrDefault(json_data, 'ID')    # assign variables from the JSON
        Text = valueOrDefault(json_data, 'Text')
        MinPrice = valueOrDefault(json_data, 'MinPrice')
        MaxPrice = valueOrDefault(json_data, 'MaxPrice')
        MinQty = valueOrDefault(json_data, 'MinQty')
        MaxQty = valueOrDefault(json_data, 'MaxQty')
        Order = valueOrDefault(json_data, 'Order')
        return jsonify(db.query(Id, Text, MinPrice, MaxPrice, MinQty, MaxQty, Order).fetchall())

def valueOrDefault(array, element, default=''):
    if element in array:
        return sqlClean(array[element], '')
    return default

def sqlClean(myvalue, default=None):      # validating strings, editing ones that may cause problems in the SQL
    if myvalue is None or myvalue == '': # if the passed value is null, keep it that way
        return default
    res = str(myvalue)  # turn the passed value into a string
    res = res.replace("'", "''") # escape ' symbols so as not to break SQL code
    res = res.replace(";", ",") # replace ; with , to avoid SQL injection
    return res

db = dbCtrl()   # set up the database script I made
app = Flask(__name__) # Launch Flask
CORS(app) # enable CORS for the app - crucial for running Python script by the Javascript
api = Api(app) # create the API
api.add_resource(Products, '/products') # create the page for everything in the Products class
api.add_resource(Product, '/product/<productid>') # create the page for the Product class
api.add_resource(Search, '/search')

if __name__ == '__main__':
    app.run(port=5002)  # run the website
