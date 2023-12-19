'''users.py is a module to manage a dictionary of users who each consist
of a dictionary.
'''

import json
import tool

file_name = 'users.json'
root_options = ('login', 'quit')
user_data = {}
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
        json.dump(user_data, file_object)

def login():
    username = tool.text_input("\nEnter your name: ")
    if username in user_data:
        print("Welcome back, " + username.title() + "!")
        return username
    else:
        user_data[username] = {}
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
        username = login()
        global active_user
        active_user = username
    else:
        print('\nSelection invalid.')


user_data = load_users()