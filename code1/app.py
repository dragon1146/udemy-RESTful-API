from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister  
from item import Item, Itemlist



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



api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
api.add_resource(UserRegister, '/register')

# debug=True will allow the source of the API to be updated and synced without restarting the API
if __name__=='__main__':
    app.run(port=5000, debug=True, host = '0.0.0.0')