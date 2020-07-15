import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required

from models.item import ItemModel





class Item(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="this field cannot be left blank"
    )

    # @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message':"there was a problem with SQL while retrieving the item."}, 500
        
        if item:
            return item.json()
        return {'message':"Item not found"}, 404 
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"An item already exist with '{}'".format(name),},400
       
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        

        try:
            item.insert()
        except:
            return {'message':"an error occurred when inserting that new item"}, 500
        
        """
        - this 'try & except' python construct will do the following
            - it will try to execute the code within the 'try' block
            - if that code does not return any error then it does not
                go into the 'execpt' portion of the code
            - if there was an error in executing the code in the
                'try' block, then python will return the message within
                the 'except' block of code
            - that message should be short but detailed enough to
                tell the programmer where in the body of the code the
                error happened
        """
        return item, 201

  
    def delete(self, name):
        if ItemModel.find_by_name(name):    
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "DELETE FROM items WHERE name=?"
            cursor.execute(query, (name,))

            connection.commit()
            connection.close()

            return {'message':"item was deleted"},200
        else:
            return {'message':"it was not deleted because it was not present"}, 404
       

    def put(self, name):
       
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        """
        this code is searching for the item in the database to see if
        it exist

        if it exist, then the 'self.update()' method will be executed
        with the values from the 'updated_item' dictionary

        if the item does not exist, then the 'self.insert()' method
        will be used to insert the item in the database with the
        values from the 'update_item()' dictionary
        """  
        updated_item = ItemModel(name, data['price'])


        if item is None:
            try:
                ItemModel.insert(updated_item)
                """
                this code will run if the item was not found in the
                database

                it will insert the item in the database with the
                values from the 'update_item()' dictionary
                """
            except:
                return {'message':"an error occurred when inserting that new item"}, 500
        else:
            try:
                ItemModel.update(updated_item)
                """
                this code will run if the item was found in the
                database

                it will update the item in the database with the
                values from the 'update_item()' dictionary
                """
            except:
                return {'message':"an error occurred when updating that new item"}, 500
        return updated_item
    

    


class Itemlist(Resource):

    # this method will return a python dictionary to the requestor with 1 key:value pair
    # the key to the pair will be the string "items"
    # the value to that key will be the "items" list which contains dictionaries with each one representing an item
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name':row[0], 'price':row[1]})
        
        connection.close()

        return {'items':items}
