 
from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}



def authenticate(username, password):
# this function will be used to match the username and password
# passed in the request to the username and password of a current
# user and return the user properties to the function that called
# upon it
    
    # this line of code was taken from the end of the section 4 video

    # user = username_table.get(username, None)
    # if user and safe_str_cmp(user.password, password):





    
    user = username_mapping.get(username, None)
        return user
    # this line takes the value of "username" passed into the
    # function and applies it to the "username_mapping.get()
    # function"
    # the "username_mapping.get(username, None)" will return the
    # python dictionary value (which will be another python
    # dictionary that represents the user property) to the key that
    # matches the value of username
    # that python dictionary that represented the user property will
    # be saved to the variable "user"
    # if there is no key in the username_mapping dictionary, then the
    # function will return "None"

def identity(payload):
# this function will be used after the user has been authenticated and has
# ... received a authentication token from the JWT object

# it will be used along with the user's authentication token
# ..."payload" to verify if the user has been authentication when that
# users makes a request

# the theory behind this is based on the fact that the token will
# ...contain a userid, if that userid in the token matches matches
# the id of an existing user then that means that that users was
# ...authenticated 

# and for a user to get an authentication token, it had to pass a
# ...valid username and password to be verified by the "authentication"
# ...function

# once the userid in the token matches an existing user in the
# ...database, then the function returns the user property of that
# user

# if the userid does not match an existing user in the database, then
# "None" is returned

    user_id = payload['identity']
    # this line of code will extract the userid from the the token
    # "payload" and save it to the variable "user_id"

    return userid_mapping.get(user_id, None)
    # once the userid in the token matches an existing user in the
    # ...database, then the function returns the user property of that
    # ...user

    # if the userid does not match an existing user in the database, then
    # ..."None" is returned
