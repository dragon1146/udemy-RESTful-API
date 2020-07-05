from flask import Flask


app = Flask(__name__)

# for now the stores and items in the stores will be stored in a list containing nested dictionaries and list
# at the start of this lesson we will start with 1 store and that store has 1 items with a price

stores = [
    {
        'name': 'my wonderful store',
        'items': [
            {
                'name': 'my item', 'price': 15.09
            }
        ]
    }
] 
# the "stores" list will contain all the stores that we are monitoring

# each store will be defined within a dictionary with the following keys...
    #name- this is the name of the store
    #this key will have a value of a string

    #items- this is a list containing all the items in that particular store
    # the items will be represented within a dictionary with the following keys


#
# 1- POST /store data: {name:}
# ...when this endpoint is received it will create a new store with the name for data

@app.route('/store', methods=['POST'])
def create_store():
    pass
    #by default an @app.route will respond to a GET request from the browser
    
    # as a result to tell the route to respond to a POST request sent from the browser you must define it with the METHOD keyword
#####################################################

##
# 2- GET /store/<string:name>
# ...when this endpoint is received, it will retreive the resources for the store with name passed as a string

@app.route('/store/<string:name>')
def get_store(name):
    pass
    # when the web app receives "/store/store-name" from the browser, it will take the string value of "store-name" and pass it into the variable "name" which is in the function "get_store"
    
    # if the string value "store-name" matches the name of a store resources in the web app then it will return a list containing the resource value of that particular store name
    
    # if the string value "store-name" does not match any of the store resources within the web app, then the web app will return a "404 error, resources not found" error
#####################################################

###
# 3- GET /store
# ... when this endpoint is received it will return the resources containing a list with all the stores

@app.route('/store')
def get_stores():
    pass
#####################################################

####
# 4- POST /store/<string:name>/item {name:, price:}
# ... when this endpoint is received it will create and item in a specific store with the item's name and its price

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass
    # the web app will receive a "/store/store-name/item" where "store-name" is one of the name of the store that is listed in the web app
#####################################################

#####
# 5- GET /store/<string:name>/item
# ... when this endpoint is received it will returen a list that contains the item(s) from that specific store

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass
#####################################################






if __name__ == '__main__':
    app.run(debug=True)