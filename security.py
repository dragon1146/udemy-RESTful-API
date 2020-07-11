 
from user import User

users = [
    User(1, 'user1', 'password1'),
]
   
username_mapping = {u.username: u for u in users}
"""[summary]
    explains the above line of code
        when used in conjunction with the "authenticate" function it
        will do the following:
        - go thru the "user" list to find a username that matches the
          value that was passed into the "authenticate" function and
          return the user account for that user (which will be in the
          form of a python dictionary)
        - the "authenticate" function will then compare the password
          string passed into the "authenticate" function to the
          password that is in the user's account
"""

userid_mapping = {u.id: u for u in users}
"""[summary]
    explains the above line of code
        when used in conjunction with the "identity" function it
        will do the following:
        - go thru the "user" list to find a userid that matches the
          value that was passed into the "identity" function and
          return the user account for that user (which will be in the
          form of a python dictionary)
"""
    



def authenticate(username, password):
# this function will be used to match the username and password
# passed in the request to the username and password of a current
# user and return the user properties to the function that called
# upon it
    
    # this line of code was taken from the end of the section 4 video

    # user = username_table.get(username, None)
    # if user and safe_str_cmp(user.password, password):

    
    user = username_mapping.get(username, None)
    if user and user.password == password:
        """ 
        this line takes the value of "username" passed into the
        function and applies it to the "username_mapping.get()" function

        this will search thru the "username_mapping" dictionary for an
        key that matches the string that the variable "username" is
        storing
        
        if it gets a match for the key, it will save the value of the
        key:value pair in the variable "user"

        the "username_mapping" dictionary stores the following:
            - key = the username of the user account "tom"
            - value = the user acount properties  "id": 2, "username": "tom", "password":
                "passwordtom"
            - example:
                username_mapping = {
                "bob": {
                "id": 1, "username": "bob", "password": "passwordbob"},
                "tom": {
                "id": 2, "username": "tom", "password":
                "passwordtom"}} 
        
        if the value for the variable "username" is "tom" for the
        function:
            "user = username_mapping.get("tom", None)"
        it will save the value for the key "tom" to the variable user

        if the function cannot find a key that matches the string stored
        in the variable "username" (in this case will be "tom"), it will
        return a "None" value

        another way to write 
            "user = username_mapping.get(username, None)"
        is
            user = username_mapping[username]
        
        the difference between the two ways is
            -if the user does not exist in the "username_mapping" when
            using "username_mapping[username]" if will return an python
            error        
            - but if the other method is used you can create a custom massage to be returned if the user does not exist    

        """
        return user
        """ 
        - this will return the account properties for the user with
          the correct match of passwords to the method that called
          it from "app.py
        - the user account properties is in the form of a python dictionary
         
         """
   
   

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
