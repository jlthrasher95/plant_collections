"""This program uses the 'users' module to store
a collection of plants in the data dictionary of any user.
"""


import users, tool


user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = tool.vertical_space + tool.dash_line + '\n\nWelcome to the '
introduction += 'Passwordless Plant Collection Builder.\nEnter "quit" at any'
introduction += 'time to quit.\n\n' + tool.dash_line
plant_type_prompt = '\nWhat type of plant would you like to add? '


def main_loop():
    """This function is the main program loop, which
    runs the root menu if no user is logged in,
    the plant menu if a valid user is logged in, or else
    ends the program with a notice about active_user.
    """
    while tool.program_running:
        if users.active_user == '':
            users.root_menu()
        elif users.active_user in users.database:
            user_data = users.database[users.active_user]
            plant_menu(user_data)
        else:
            users.invalid_active_user()

def plant_menu(user_data):
    """This function evaluates the selection for a logged in user."""
    selection = tool.menu(user_options)
    if selection == 'quit' or selection == 'q':
        tool.end_run()
    elif selection == 'logout' or selection == 'l':
        users.logout()
    elif selection == 'add plant' or selection == 'a':
        add_plant(user_data)
    elif selection == 'view plants' or selection == 'v':
        view_plants(user_data)
    else:
        print('\nSelection invalid.')

def add_plant(user_data):
    """This function adds a new plant to the database."""
    plant_type = tool.caseless_input(plant_type_prompt)
    if plant_type == 'quit':
        tool.end_run()
    while tool.program_running:
        plant_name = tool.caseless_input("\nWhat's this plant's name? ")
        if plant_name == 'quit':
            tool.end_run()
        elif plant_name in user_data.keys():
            print('\nYou already have a plant named ' + plant_name + '!')
            continue
        else:
            # This adds a plant to the user's data as {name : type}.
            user_data[plant_name] = plant_type
            users.save_users()
            print('Added a ' + plant_type +
                  ' named ' + plant_name.title() + '.')
            break

def view_plants(user_data):
    """This function lists all of a user's plants."""
    print('\n' + users.active_user.title() + ' has the following plants:')
    for plant_name in user_data:
        print(plant_name.title() + ' the ' + user_data[plant_name])


print(introduction)
main_loop()