# !/usr/bin/env python
# -----------------------------------------------------------------
# Script     : utils.py
# Type       : class
# Purpose    : Simple project which allows GET, POST, DELETE and PUT methods
# Inputs     : Use Postman to call the API URL
# Ouput      : Result of API calls
# Author     : Ashish Anand
# Created on : 21-Feb-2019
# Version    : 0.1
# -----------------------------------------------------------------
# Bug History:
# <Date Modified>  < By whom>    <What is the Change>
#
# -----------------------------------------------------------------


from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    """
    Contains all the method calls for the API
    """
    def get(self, name):
        """
        Retrieve the list of items
        :param name: item name to be retrieved
        :return:
        """
        for item in items:
            if item['name'] == name:
                return item
        return {"item" : None}, 404

    def post(self, name):
        """
        Add an item to the list of items
        :param name: Name of item to be added
        :return:
        """
        sent_data = request.get_json()
        item = {"name" : name, "price" : sent_data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        """
        Delete an item from the list of items
        :param name: name of item to be deleted
        :return:
        """
        for item in items:
            if item['name'] == name:
                items.remove(item)
        return {"message" : "item deleted"}

    def put(self, name):
        """
        Update / Create an item in the list
        :param name: name of item to be created / updated
        :return:
        """
        sent_data = request.get_json()
        for item in items:
            if item['name'] == name:
                item['price'] = sent_data['price']
                return item


class ItemList(Resource):
    """
    Retrieve complete set of items from the item list
    """
    def get(self):
        """
        Retrieve all items from the list
        :return:
        """
        return {"items_total" : items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if __name__ == '__main__':
    app.run(debug=True)


