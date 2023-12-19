import users, tool

user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = tool.vertical_space + tool.dash_line
introduction += '\n\nWelcome to the Passwordless Plant Collections Manager.'
introduction += '\nEnter "quit" at any time to quit.'
introduction += '\n\n' + tool.dash_line


def main_loop():
    """main() is the main program loop, which shows options depending
    on whether or not a valid user is logged in and passes the user's
    selection to the appropriate menu.
    """
    while tool.run_flag:
        if users.active_user == '':
            users.root_menu()
        elif users.active_user in users.user_data:
            user_menu()
        else:
            users.invalid_user_flag()

def user_menu():
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
    user = users.user_data[users.active_user]
    type = tool.text_input('\nWhat type of plant would you like to add? ')
    while tool.run_flag:
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
    user = users.user_data[users.active_user]
    print('\n' + users.active_user.title() + ' has the following plants:')
    for plant in user:
        print('\tA ' + user[plant] + ' named ' + plant.title())


print(introduction)
main_loop()