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
        item = self.find_by_name(name)
        """
        this code is searching for the item in the database to see if
        it exist

        if it exist, then the 'self.update()' method will be executed
        with the values from the 'updated_item' dictionary

        if the item does not exist, then the 'self.insert()' method
        will be used to insert the item in the database with the
        values from the 'update_item()' dictionary
        """  
        updated_item = {'name':name, 'price':data['price']}


        if item is None:
            try:
                self.insert(updated_item)
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
                self.update(updated_item)
                """
                this code will run if the item was found in the
                database

                it will update the item in the database with the
                values from the 'update_item()' dictionary
                """
            except:
                return {'message':"an error occurred when updating that new item"}, 500
        return updated_item
    

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        """
        - this SQL command will update the items table and set the
            price column value to the updated price where the name of
            the item in the row is equal to the variable 'name'
        """
        
        
        cursor.execute(query, (item['price'], item['name']))
        """
        - the order in which we sent the values for the name and price
        of the item is defferent from anywhere else in the code

        - this is because in the variable 'query' the value of price
            comes before the value of the name of the item

        - so we must follow the order in which SQL command will be executed
        """

        connection.commit()
        connection.close()

    


class Itemlist(Resource):

    # this method will return a python dictionary to the requestor with 1 key:value pair
    # the key to the pair will be the string "items"
    # the value to that key will be the "items" list which contains dictionaries with each one representing an item
    def get(self):
        return {'items':items}
