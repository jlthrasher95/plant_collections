"""This is a module to handle storing a dictionary of users in a JSON
file. Each user's data is a dictionary."""

import json
import tool

file_name = 'users.json'
root_options = ('login', 'quit')
database = {}
active_user = ''


def load_users():
    """This returns a dictionary of users from a JSON file if it exists,
    or else returns an empty dictionary.
    """
    try:
        with open(file_name) as file_object:
            users_dict = json.load(file_object)
    except FileNotFoundError:
        return {}
    else:
        return users_dict
    
def save_users():
    """This writes the user dictionary to the JSON file."""
    with open(file_name, 'w') as file_object:
        json.dump(database, file_object)

def login():
    """This lets you select or create a user."""
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
    """This clears active_user and prints a message."""
    global active_user
    active_user = ''
    print('Logging out.')

def invalid_active_user():
    """invalid_active_user() is used in case active_user has been set to a
    value other than a registered user.
    """
    print("active_user invalid")
    quit()

def root_menu():
    """This allows the user to quit or login."""
    selection = tool.menu(root_options)
    if selection == 'quit' or selection == 'q':
        tool.quit()
    elif selection == 'login' or selection == 'l':
        global active_user
        active_user = login()
    else:
        print('\nSelection invalid.')


# This loads the dictionary of users when the module is imported.
database = load_users()