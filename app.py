from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jose'

jwt = JWT(app, authenticate, identity)
"""the jwt function will be created from the JWT class and it will take 3 arguments
    - the entire app
    - the "authenticate" function in the security.py file
    - the "identity" function in the security.py file
    
    - the explaination for the above functions are found in
        the "security.py" file

the jwt object will be used to do the following:
    - authenticate the user with the "authenticate" functioin
    - verify if the user that is sending a request has already
        been authenticated by using the "identity" function

    - the explaination for the above functions are found in
            the "security.py" file


"""


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
        # if the item is not in the items list, it will return a 404
        # return status code and a null string will be displayed
    
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="this field cannot be left blank"
    )

    # @jwt_required()
    def get(self, name):
        # the line of code below can be used instead of the "for
        # loop" and the "if" conditional statement
        # both methods goes thru the item in items and find a match
        # to an item that matches the name in the URL for the request
        # the method will still return a python dictionary of the
        # item
        # if an item is not in the items list, the API will return a
        # 404 error
        """  # item = next(filter(lambda x: x['name'] == name, items),
        # None)
            # return {'item': item}, 200 if item else 404 """

        

        
        for item in items:
            if item['name'] == name:
                return item
        return {'item':None}, 404

    
    
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

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')

# debug=True will allow the source of the API to be updated and synced without restarting the API
app.run(port=5000, debug=True, host = '0.0.0.0')