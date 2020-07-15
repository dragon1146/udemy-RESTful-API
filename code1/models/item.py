import sqlite3


"""
these methods will be used to represent the items while they are
being interacted with within the API, away from the observation of
the user

once again, these method should not contain any 'CRUD' methods
"""

"""
in the course of this video, all the classmethod that were copied
over from the resourse package were converted into regular methods

to understand this you need to understand where the classmethod were
created when it was in the resources package

basically the classmethod created an object that represented the item
that was passed to the API from the user

with that oject created from the classmethod, the API can use it and
do whatever it wants with it without affecting the integrity of the
data

this class is doing the samething

when the item resources is called, there is a line in the code that
creates a ItemModel object of that item in which the API can now do
what ever it wants to do with that object
"""

class ItemModel:
    def __init__(self, name, price):
      self.name = name
      self.price = price
      """
      this method will create an object of the item to be used within
      the API to do its work
      """ 
 
    def json(self):
      return {'name':self.name, 'price':self.price}    
        """
        this above method will return a json representation of the item
        """

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (self.name, self.price))

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
    
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
    
    
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        """
        - this SQL command will update the items table and set the
            price column value to the updated price where the name of
            the item in the row is equal to the variable 'name'
        """
        
        
        cursor.execute(query, (self.price, self.name))
        """
        - the order in which we sent the values for the name and price
        of the item is defferent from anywhere else in the code

        - this is because in the variable 'query' the value of price
            comes before the value of the name of the item

        - so we must follow the order in which SQL command will be executed
        """

        connection.commit()
        connection.close()
