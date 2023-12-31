"""This program is a frontend for the users module to store plants
in users' dictionaries of data. Each plant has an arbitrary name and
type.
"""


import tool, users


file_name = 'users.json'
introduction = tool.vertical_space + tool.dash_line + '\n\nWelcome to the '
introduction += 'Passwordless Plant Collection Builder.\nEnter "quit" at any'
introduction += 'time to quit.\n\n' + tool.dash_line

def add_plant():
    """This function adds a plant to the user's data."""
    type = set_plant_type()
    if type:
        name = set_plant_name()
        if name:
            session.add_to_user(name, type)
            print('Added a ' + type + ' named ' + name.title() + '.')

def set_plant_type():
    """This function prompt for a plant type and returns it."""
    type_prompt = "\nEnter this plant's type, or 'back' to cancel: "
    type = None
    while session.running:
        if type:
            if type in ('back', 'b'):
                print('Plant addition canceled.')
                return None
            else:
                return type
        type = session.user_input(type_prompt)

def set_plant_name():
    """This function prompt for a plant name and returns it."""
    name_prompt = "\nEnter this plant's name, or 'back' to cancel: "
    name = None
    while session.running:
        if name:
            if name in ('back', 'b'):
                print('Plant addition canceled.')
                return None
            elif name in session.user_data:
                print('\nYou already have a plant named ' + name + '!')
            else:
                return name
        name = session.user_input(name_prompt)

def remove_plant():
    """This function removes a plant from the user's collection."""
    prompt = "\nEnter the name of the plant to remove, or 'back' to cancel: "
    name = None
    while session.running:
        if name:
            if name in ('back', 'b'):
                print("Removal canceled.")
                return False
            elif name in session.user_data:
                session.delete_from_user(name)
                print(name + " removed.")
                return True
            else:
                print("You don't have any plants named " + name + "!")
        name = session.user_input(prompt)

def view_plants():
    """This function lists all of a user's plants."""
    print('\n' + session.user.title() + ' has the following plants:')
    for plant in session.user_data:
        print(plant.title() + ' the ' + session.user_data[plant])


session = users.Session(file_name)

root_options = {('quit', 'q') : session.end,
                ('login', 'l') : session.sign_in,
                ('add user', 'add', 'a') : session.sign_up,
                ('remove user', 'remove', 'r') : session.remove_user,
                ('view users', 'view', 'v') : session.view_users,
                }

user_options = {('quit', 'q') : session.end,
                ('logout', 'l') : session.logout,
                ('add plant', 'add', 'a') : add_plant,
                ('remove plant', 'remove', 'r') : remove_plant,
                ('view plants', 'view', 'v') : view_plants,
                ('change username', 'change', 'c') : session.change_name,
                }


print(introduction)
while session.running:
    if session.user:
        tool.menu(user_options)
    else:
        tool.menu(root_options)