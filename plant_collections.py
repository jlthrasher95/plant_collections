"""This program is a frontend for the users module to store plants
in users' dictionaries of data. Each plant has an arbitrary name and
type.
"""


import tool
from users import Session


file_name = 'users.json'
root_options = ('login', 'quit')
user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = tool.vertical_space + tool.dash_line + '\n\nWelcome to the '
introduction += 'Passwordless Plant Collection Builder.\nEnter "quit" at any'
introduction += 'time to quit.\n\n' + tool.dash_line


def root_menu():
    """This function allows the user to quit or login."""
    selection = tool.menu(root_options)
    if selection == 'quit' or selection == 'q':
        session.end()
    elif selection == 'login' or selection == 'l':
        session.login()
    else:
        print('\nSelection invalid.')

def plant_menu():
    """This function evaluates the selection for a logged in user."""
    selection = tool.menu(user_options)
    if selection == 'quit' or selection == 'q':
        session.end()
    elif selection == 'logout' or selection == 'l':
        session.logout()
    elif selection == 'add plant' or selection == 'a':
        add_plant()
    elif selection == 'view plants' or selection == 'v':
        view_plants()
    else:
        print('\nSelection invalid.')

def add_plant():
    """This function adds a new plant to the database."""
    type = tool.text_input('\nWhat type of plant would you like to add? ')
    if type == 'quit':
        session.end()
    while session.running:
        name = tool.text_input("\nWhat's this plant's name? ")
        if name == 'quit':
            session.end()
        elif name in session.user.data:
            print('\nYou already have a plant named ' + name + '!')
        else:
            session.user.add_data(name, type)
            print('Added a ' + type + ' named ' + name.title() + '.')
            break

def view_plants():
    """This function lists all of a user's plants."""
    print('\n' + session.user.name.title() + ' has the following plants:')
    for plant in session.user.data:
        print(plant.title() + ' the ' + session.user.data[plant])


print(introduction)
session = Session(file_name)
while session.running:
    if session.user:
        plant_menu()
    else:
        root_menu()
