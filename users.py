"""This module handles a dictionary of users who each have a dictionary
for user data. The dictionary of users is loaded from and saved to a
JSON file.
"""


import json
import tool


users_file = 'users.json'
root_options = ('login', 'quit')
database = {}
active_user = ''


def load_users():
    """This function returns a dictionary of users from a JSON file if
    it exists, or else returns an empty dictionary.
    """
    try:
        with open(users_file) as file_object:
            users_dict = json.load(file_object)
    except FileNotFoundError:
        return {}
    else:
        return users_dict
    
    
def save_users():
    """This function writes the user dictionary to the JSON file."""
    with open(users_file, 'w') as file_object:
        json.dump(database, file_object)


def login():
    """This function selects or creates a user and
    returns the chosen username.
    """
    global active_user
    active_user = tool.caseless_input("\nEnter your name: ")
    if active_user == 'quit':
        tool.end_run()
    elif active_user in database:
        print("Welcome back, " + active_user.title() + "!")
    else:
        database[active_user] = {}
        save_users()
        print("\nNew user created: " + active_user)
        print("\nWelcome, " + active_user.title() + ".")


def root_menu():
    """This function allows the user to quit or login."""
    selection = tool.menu(root_options)
    if selection == 'quit' or selection == 'q':
        tool.end_run()
    elif selection == 'login' or selection == 'l':
        login()
    else:
        print('\nSelection invalid.')
    
    
def logout():
    """This function clears active_user and prints a message."""
    global active_user
    active_user = ''
    print('Logging out.')


def invalid_active_user():
    """This function is run in case active_user has been set to
    a value other than a registered user.
    """
    print("active_user invalid")
    tool.end_run()


# This loads the dictionary of users when the module is imported.
database = load_users()