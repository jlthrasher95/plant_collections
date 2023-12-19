import users, tool

user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = tool.vertical_space + tool.dash_line + '\n\nWelcome to the '
introduction += 'Passwordless Plant Collection Builder.\nEnter "quit" at any'
introduction += 'time to quit.\n\n' + tool.dash_line


def main_loop():
    """This is the main program loop, which shows options depending
    on whether or not a valid user is logged in and passes the user's
    selection to the appropriate menu or an error message.
    """
    while tool.program_running:
        if users.active_user == '':
            users.root_menu()
        elif users.active_user in users.database:
            plant_menu()
        else:
            users.invalid_active_user()

def plant_menu():
    """This evaluates the selection for a logged in user."""
    selection = tool.menu(user_options)
    if selection == 'quit' or selection == 'q':
        tool.quit()
    elif selection == 'logout' or selection == 'l':
        users.logout()
    elif selection == 'add plant' or selection == 'a':
        add_plant()
    elif selection == 'view plants' or selection == 'v':
        view_plants()
    else:
        print('\nSelection invalid.')

def add_plant():
    """This adds a new plant to the database."""
    user = users.database[users.active_user]
    type = tool.text_input('\nWhat type of plant would you like to add? ')
    if type == 'quit':
        tool.quit()
    while tool.program_running:
        name = tool.text_input("\nWhat's this plant's name? ")
        if name == 'quit':
            tool.quit()
        elif name in user.keys():
            print('\nYou already have a plant named ' + name + '!')
            continue
        else:
            user[name] = type
            users.save_users()
            print('Added a ' + type + ' named ' + name.title() + '.')
            break

def view_plants():
    """This lists all of a user's plants."""
    user = users.database[users.active_user]
    print('\n' + users.active_user.title() + ' has the following plants:')
    for plant in user:
        print(plant.title() + ' the ' + user[plant])


print(introduction)
main_loop()