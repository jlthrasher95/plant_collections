"""plant_collections.py stores a dictionary of users, each with their
own dictionary for plants. Every plant has an arbitrary name and type,
and plants can be added or viewed as a list.
"""

from users import load_users, save_users, login
from tool import text_input, list_options

users_file = 'users.json'
root_options = ('login', 'quit')
user_options = ('add plant', 'view plants', 'logout', 'quit')
introduction = '\n\n\n\n\n\n\n\n\n\n\n\n--------------------------------'
introduction += '--------------------------------'
introduction += '\n\nWelcome to the Passwordless Plant Collections Manager.'
introduction += '\nEnter "quit" at any time to quit.'
introduction += '\n\n--------------------------------'
introduction += '--------------------------------'
quit_flag = False
user_flag = ''


def quit():
    global quit_flag
    quit_flag = True
    print('\nExiting program.')

def logout():
    global user_flag
    user_flag = ''
    print('Logging out.')

def invalid_user_flag():
    """invalid_user_flag() is used in case user_flag has been set to a value
    other than a registered user.
    """
    print("user_flag invalid")
    quit()

def menu():
    """menu() is the main program loop, which shows options depending
    on whether or not a valid user is logged in and passes the user's
    selection to the appropriate menu.
    """
    while quit_flag == False:
        if user_flag == '':
            options_list = root_options
            selection = list_options(options_list)
            root_menu(selection)
        elif user_flag in users:
            options_list = user_options
            selection = list_options(options_list)
            user_menu(selection)
        else:
            invalid_user_flag()

def root_menu(selection):
    if selection == 'quit' or selection == 'q':
        quit()
    elif selection == 'login' or selection == 'l':
        username = login(users, users_file)
        global user_flag
        user_flag = username
    else:
        print('\nSelection invalid.')


def user_menu(selection):
    if selection == 'quit' or selection == 'q':
        quit()
    elif selection == 'logout' or selection == 'l':
        logout()
    elif selection == 'add plant' or selection == 'a':
        add_plant()
    elif selection == 'view plants' or selection == 'v':
        view_plants()
    else:
        print('\nSelection invalid.')

def add_plant():
    user = users[user_flag]
    #sets value of "user" to be this user's dictionary of data
    type = text_input('\nWhat type of plant would you like to add? ')
    while True:
        name = text_input("\nWhat's this plant's name? ")
        if name == 'quit':
            quit()
            break
        elif name in user.keys():
            print('\nYou already have a plant named ' + name + '!')
            continue
        else:
            user[name] = type
            #adds plant name to user's dictionary with type as value
            save_users(users, users_file)
            #saves changes
            print('Added a ' + type + ' named ' + name.title() + '.')
            break

def view_plants():
    user = users[user_flag]
    #sets value of "user" to be this user's dictionary of data
    print('\n' + user_flag.title() + ' has the following plants:')
    for plant in user:
        print('\tA ' + user[plant] + ' named ' + plant.title())
        #prints formatted type (value of user[plant]) and name of each plant


users = load_users(users_file)
#load or create a dictionary for user data

print(introduction)
#print formatted introduction

menu()
#run main menu loop