"""This program is a frontend for the users module to store plants
in users' dictionaries of data. Each plant has an arbitrary name and
type.
"""


import tool
import users

file_name = 'users.json'
introduction = tool.vertical_space + tool.dash_line + '\n\nWelcome to the '
introduction += 'Passwordless Plant Collection Builder.\nEnter "quit" at any'
introduction += 'time to quit.\n\n' + tool.dash_line


def add_plant():
    """This function adds a new plant to the user's data."""
    type = tool.caseless_input('\nWhat type of plant would you like to add? ')
    if type == 'quit':
        session.end()
    while session.running:
        name = tool.caseless_input("\nWhat's this plant's name? ")
        if name == 'quit':
            session.end()
        elif name in session.user_data:
            print('\nYou already have a plant named ' + name + '!')
        else:
            session.add_to_user(name, type)
            print('Added a ' + type + ' named ' + name.title() + '.')
            break

def view_plants():
    """This function lists all of a user's plants."""
    print('\n' + session.user.title() + ' has the following plants:')
    for plant in session.user_data:
        print(plant.title() + ' the ' + session.user_data[plant])

session = users.Session(file_name)
root_options = {'quit' : session.end, 'q' : session.end,
             'login' : session.login, 'l' : session.login,
             }
user_options = {'quit' : session.end, 'q' : session.end,
              'logout' : session.logout, 'l' : session.logout,
              'add plant' : add_plant, 'a' : add_plant,
              'view plants' : view_plants, 'v' : view_plants,
              }


print(introduction)
while session.running:
    if session.user:
        tool.menu(user_options)
    else:
        tool.menu(root_options)
