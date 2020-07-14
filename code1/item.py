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

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0], 'price':row[1]}}
        return {'message':"Item not found"}, 404

        





    
    
    def post(self, name):
        """ 
        - this method with append an item with its properties to the
        items list it will get the name of the item from the URL and
        the properties of the item will be in json format in the body of the request
        
        - once the item and its properties have been added to the list, the API will return the tems and its properties to the requester
        """

        
        data = Item.parser.parse_args()
        """
        - the method being used will extract the json date from the request and convert it to a python dictionary and save it to the variable "data"
        - if you are not sure if the request from the client will be in a json format, you can use an switch in the method called 
             "request.get_json(force=True)" 
            which will accept any data in the body of the request whether it is in json format or not
        - this switch will not look in the "Content-Type" header field to see if it is set to "application/json"
        - this is a posible vulnerability in the code because it will process whatever data that's in the body even if its not inn json format
        - another switch you can use to prevent the API from returning an error is 
            "request.get_json(silent=True)"
        - this will not return an error if the wrong content-type is in the header, but it will return an "null" value
            item = next(filter(lambda x: x['name'] == name, items),
            None)
        return {'message': "an item with the name{} already
        exist.".format(name)}, 400 
        """
        
       
        item = {'name': name, 'price': data['price']}
        """
         this code will extract the price of the item that was sent in the body of the request in json format but was later converted to a python dictionary

        in ('name': name,), the name without the quotes is a variable that has the value that was passed in the URL of the request
            "http://127.0.0.1:5000/chair"
        in this case this request will create a new item called "chair" with one parameter of "price" with its value of "data['price']"
        """
        
        
        items.append(item)
        """
        this list method that allows you to append a list item to the end of the existing items
        """
        
        return item, 201
        """
        this is returning the items and its properties to the
        requester and also a return status code of "200" which means
        that something was created successfully
        """

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

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
