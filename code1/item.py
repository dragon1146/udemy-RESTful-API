import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required




class Item(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="this field cannot be left blank"
    )

    # @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message':"Item not found"}, 404 
    
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0], 'price':row[1]}}
    
    def post(self, name):
        if self.find_by_name(name):
            return {'message':"An item already exist with '{}'".format(name),},400
       
        data = Item.parser.parse_args()
       
        item = {'name': name, 'price': data['price']}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

        return item, 201
       
    def delete(self, name):
        # if self.find_by_name(name):
        #     return {'message':"An item already exist with '{}'".format(name),},400
       
        
       
        # item = self.find_by_name(name)

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message':"item was deleted"},200
       

    def put(self, name):
       
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)

        return item

    


class Itemlist(Resource):

    # this method will return a python dictionary to the requestor with 1 key:value pair
    # the key to the pair will be the string "items"
    # the value to that key will be the "items" list which contains dictionaries with each one representing an item
    def get(self):
        return {'items':items}