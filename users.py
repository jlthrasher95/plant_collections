'''users.py is a module to store functions pertaining to users'''

import json
#import json module for storing dictionary of users

from tool import text_input
#text_input() solicits user input and converts it to a lowercase string


def load_users(filename):
    try:
    #attempt to open the users file, but prepare for exceptions

        with open(filename) as file_object:
        #load file contents into file_object then close file when done using it

            users_dict = json.load(file_object)
            #decode JSON data into a python dictionary

    except FileNotFoundError:
        return {}
    #return an empty dictionary if users file is not found

    else:
        return users_dict
    #return dictionary of users provided that one was found

    
def save_users(users_dict, filename):
    with open(filename, 'w') as file_object:
    #open file in write-mode and close when done

        json.dump(users_dict, file_object)
        #encode dictionary as JSON and overwrite users file

def login(users_dict, filename):
    username = text_input("\nEnter your name: ")
    #request name from user and convert to lowercase string

    if username in users_dict:
        print("Welcome back, " + username.title() + "!")
        return username
    #greet repeat user and return their name

    else:
        users_dict[username] = {}
        #add new user with an empty dictionary as its value

        save_users(users_dict, filename)
        #save modified dictionary of users

        print("\nNew user created: " + username)
        print("\nWelcome, " + username.title() + ".")
        return username
        #show that new user was created, greet new user, and return username