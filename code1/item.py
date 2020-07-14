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
        try:
            item = self.find_by_name(name)
        except:
            return {'message':"there was a problem with SQL while retrieving the item."}, 500
        
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
        

        try:
            self.insert(item)
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

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()
        """
        - this 'classmethod' will be used by the 'post' and 'put'
        method to insert items or update items in the database
        
        - the code could have stayed in the 'post' method but when
          the 'put' method calls up the 'post' method to insert an
          item into the database, there will be code that will be
          executed that is not needed to be executed by the 'put'
          method

        - instead of taking the name of a item as a variable, this
          method will take an item with its properties
        
        """
       
    def delete(self, name):
        if self.find_by_name(name):    
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
