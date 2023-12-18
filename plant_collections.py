"""plant_collections.py stores a dictionary of users, each with their
own dictionary for plants. Every plant has an arbitrary name and type,
and plants can be added or viewed as a list.
"""


import users, tool


root_options = ('login', 'quit')
user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = '\n\n\n\n\n\n\n\n\n\n\n\n--------------------------------'
introduction += '--------------------------------'
introduction += '\n\nWelcome to the Passwordless Plant Collections Manager.'
introduction += '\nEnter "quit" at any time to quit.'
introduction += '\n\n--------------------------------'
introduction += '--------------------------------'


def main():
    """main() is the main program loop, which shows options depending
    on whether or not a valid user is logged in and passes the user's
    selection to the appropriate menu.
    """
    while tool.run_flag:
        if users.active_user == '':
            selection = tool.menu(root_options)
            root_menu(selection)
        elif users.active_user in users.user_data:
            selection = tool.menu(user_options)
            user_menu(selection)
        else:
            users.invalid_user_flag()

def root_menu(selection):
    if selection == 'quit' or selection == 'q':
        tool.quit()
    elif selection == 'login' or selection == 'l':
        username = users.login(users.user_data, users.file_name)
        users.active_user = username
    else:
        print('\nSelection invalid.')


def user_menu(selection):
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
    user = users.user_data[users.active_user]
    type = tool.text_input('\nWhat type of plant would you like to add? ')
    while True:
        name = tool.text_input("\nWhat's this plant's name? ")
        if name == 'quit':
            tool.quit()
            break
        elif name in user.keys():
            print('\nYou already have a plant named ' + name + '!')
            continue
        else:
            user[name] = type
            users.save_users(users.user_data, users.file_name)
            print('Added a ' + type + ' named ' + name.title() + '.')
            break

def view_plants():
    user = users.user_data[users.active_user]
    print('\n' + users.active_user.title() + ' has the following plants:')
    for plant in user:
        print('\tA ' + user[plant] + ' named ' + plant.title())


print(introduction)
main()