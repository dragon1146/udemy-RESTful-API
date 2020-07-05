from flask import Flask,jsonify,request,render_template

app = Flask(__name__)
#####################################################

# for now the stores and items in the stores will be stored in a list containing nested dictionaries and list
# at the start of this lesson we will start with 1 store and that store has 1 items with a price

stores = [
  {
    'name': 'bata',
    'items': 
    [{'name':'my item', 'price': 15.99 }]
}
]

# the "stores" list will contain all the stores that we are monitoring

# each store will be defined within a dictionary with the following keys...
    #name- this is the name of the store
    #this key will have a value of a string

    #items- this is a list containing all the items in that particular store
    # the items will be represented within a dictionary with the following keys
#####################################################


#####################################################
# this route decorator will render the index.html homepage located in the pwd/templates/

@app.route('/')
def home():
  return render_template('index.html')
#####################################################

#####################################################
#post /store data: {name :}
# 1- POST /store data: {name:}
# ...when this endpoint is received it will create a new store with the name in the resouce section of the URI
@app.route('/store' , methods=['POST'])
def create_store():
    
  request_data = request.get_json()
  # the request.get_json() function will extract the json payload from  the request sent by the client's browser
    # this results from the function will be saved in the variable "request_data"
    # the data returned from the function will be in the form of a python dictionary
  new_store = {
    'name':request_data['name'],
    'items':[]
  }

  stores.append(new_store)
  return jsonify(new_store)
  
#####################################################


#####################################################
# this route is used to get the properties of a particular store
#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
        #   this is a flask method that takes the value from the "stores" list which is a python dictionary formate(data type) and converts it into a json format
        #   this is done because the client's browser and the app have already established that data within the http body will be in a json format, this function achieves this
        #   if the client's browser would send request with data in the body of the http that is not in a json format, the app will return a 500 series error message to the client's browser indicating that the problem was caused by the client
  return jsonify ({'message': 'store not found'})
  #pass
#####################################################



#####################################################

# this route will return in json format a list of all the stores and thier items with the item properties
#get /stores
@app.route('/stores')
def get_stores():
  return jsonify({'stores': stores})

# this route will add a new item in the store with its name in the URI
# the properties of the item will be in the body of the request
# "request.get_json" is a method that will extract the properties of the item from the request which will be in json format
# the "request.get_json" method will return a python dictionary equal to the json data in the request body

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})

#####################################################



#####################################################
# this route will return the properties of an item from a particular store
# the "jsonify" method is used to do the opposite of the "request.get_json" method; it will return a json formated version of the python dictionary used to store the item properties

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

app.run(port=5000)