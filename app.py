from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []
class Item(Resource):
    # this method will retreive the item and its properties and return it to the requester
    # the name of the item being requested will be in the URL of the request
    # the method does that by
        # looping thru the item in items
        # each item in the list will be a python dictionary, so during the loop, the "item" variable will represent 1 dictionary at a time
        # therefor the explaination to the "if" statement is:
            
            # items = [{'name':'piano, 'price': 20}, {'name':'chair, 'price': 30}]

            # during the first interation of the loop the "item" variable will be equal to 
                # item = {'name':'piano, 'price': 20}
            
            # then the loop falls into the "if" statement portion of the method which evaluates
                
                # during the time that "item = {'name':'piano, 'price': 20}" if there is a value of a key:value pair that matches "chair" then the API will return the entire dictionary which will be the dictionary that represents the item's name in the URL

                # at the time "item = {'name':'piano, 'price': 20}", there is no value of a key:value pair that matches to "chair", so the loop goes to the next dictionary that represents an item and equate it to "item"
                    # item = {'name':'chair, 'price': 30}
                
                # the loop then falls into the "if" statement again and evaluates for the value "chair"

                # this time the dictionary does have a value to a key:value pair that is equal to "chair"

                # the endpoint then returns the dictionary that the "item" variable represented when the "if" statement was True

                # when the "if" statement was not True like in the first interation, the API will
                
                    # return {'item':None}, 404
                
                    # this will return a value of "null" and a "404" return status code
        
        # if the name in the URL matches the name of an item in the list, then that item will be returned with its name and properties
        # if the item is not in the items list, it will return a 404 return status code and a null string will be displayed
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item':None}, 404

    
    # this method with append an item with its properties to the items list
    # it will get the name of the item from the URL and the properties of the item will be in json format in the body of the request
    # once the item and its properties have been added to the list, the API will return the tems and its properties to the requester
    def post(self, name):
        
        # this is a static way of passing an item and its properties to the API
        # on a properly written code, the code within "{}" will be extracted from the request body by a method called "request.get_json"
        item = {'name': name, 'price': 12.00}
        
        # list method that allows you to append a list item to the end of the existing items
        items.append(item)
        
        # this is return the items and its properties to the requester and also a return status code of "200" which means that something was created successfully
        return item, 201


api.add_resource(Item, '/item/<string:name>') 

app.run(port=5000)