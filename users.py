'''users.py is a module to manage a dictionary of users who each consist
of a dictionary.
'''

import json
import tool

file_name = 'users.json'
root_options = ('login', 'quit')
database = {}
active_user = ''


def load_users():
    try:
        with open(file_name) as file_object:
            users_dict = json.load(file_object)
    except FileNotFoundError:
        return {}
    else:
        return users_dict
    
def save_users():
    with open(file_name, 'w') as file_object:
        json.dump(database, file_object)

def login():
    username = tool.text_input("\nEnter your name: ")
    if username in database:
        print("Welcome back, " + username.title() + "!")
        return username
    else:
        database[username] = {}
        save_users()
        print("\nNew user created: " + username)
        print("\nWelcome, " + username.title() + ".")
        return username
    
def logout():
    global active_user
    active_user = ''
    print('Logging out.')

def invalid_user_flag():
    """invalid_user_flag() is used in case active_user has been set to a
    value other than a registered user.
    """
    print("active_user invalid")
    quit()

def root_menu():
    selection = tool.menu(root_options)
    if selection == 'quit' or selection == 'q':
        tool.quit()
    elif selection == 'login' or selection == 'l':
        global active_user
        active_user = login()
    else:
        print('\nSelection invalid.')


database = load_users()