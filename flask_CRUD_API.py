from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [{'name': 'TV', 'price': 19.99}, {'name': 'Sofa', 'price': 20.01}]


class GetAllItems(Resource):
    def get(self):
        return {'item': items}


class GetAnItem(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
            return {'item': 'Not Found'}, 404

class AddAnItem(Resource):
    def post(self):
        input = request.get_json()
        items.append(input)
        return input, 201

class DeleteAnItem(Resource):
    def delete(self, name):
        global items
        l = []
        for item in items:
            if item['name'] != name:
                l.append(item)
        items = l
        return {'items': l}

class UpdateAnItem(Resource):
    def put(self, name):
        input = request.get_json()
        for item in items:
            if item['name'] == input['name']:
                item['price'] = input['price']
        return {'item': items}

api.add_resource(GetAllItems, "/getAll")
api.add_resource(GetAnItem, "/getItem/<string:name>")
api.add_resource(AddAnItem, "/addItem")
api.add_resource(DeleteAnItem, "/delItem/<string:name>")
api.add_resource(UpdateAnItem, '/updateItem/<string:name>')


app.run(debug=True)
