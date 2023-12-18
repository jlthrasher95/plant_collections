'''users.py is a module to store functions pertaining to users'''

import json
import tool

file_name = 'users.json'
user_data = {}
active_user = ''

def load_users(filename):
    try:
        with open(filename) as file_object:
            users_dict = json.load(file_object)
    except FileNotFoundError:
        return {}
    else:
        return users_dict
    
def save_users(users_dict, filename):
    with open(filename, 'w') as file_object:
        json.dump(users_dict, file_object)

def login(users_dict, filename):
    username = tool.text_input("\nEnter your name: ")
    if username in users_dict:
        print("Welcome back, " + username.title() + "!")
        return username
    else:
        users_dict[username] = {}
        save_users(users_dict, filename)
        print("\nNew user created: " + username)
        print("\nWelcome, " + username.title() + ".")
        return username
    
def logout():
    global active_user
    active_user = ''
    print('Logging out.')

def invalid_user_flag():
    """invalid_user_flag() is used in case active_user has been set to a value
    other than a registered user.
    """
    print("active_user invalid")
    quit()


user_data = load_users(file_name)