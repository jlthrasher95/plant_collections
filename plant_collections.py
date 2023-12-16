from users import load_users, save_users, login
#custom functions for working with user dictionary in JSON file

from tool import text_input, list_options
#convenience functions


users_file = 'users.json'
#filename for storing user data

introduction = '\n\n\n\n\n\n\n\n\n\n\n\n--------------------------------'
introduction += '--------------------------------'
introduction += '\n\nWelcome to the Passwordless Plant Collections Manager.'
introduction += '\nEnter "quit" at any time to quit.'
introduction += '\n\n--------------------------------'
introduction += '--------------------------------'
#formatted introduction text

root_options = ('login', 'quit')
user_options = ('add plant', 'view plants', 'logout', 'quit')
#options to be listed

quit_flag = False
user_flag = ''
#flags for controlling quit status and active user


def quit():
    #sets quit_flag to True and prints an exit message
    global quit_flag
    '''
    Python's "global" keyword tells a function to set the value of a variable 
    for the whole program, rather than creating an in-function variable with 
    the same name.
    '''

    quit_flag = True
    print('\nExiting program.')


def logout():
    #sets user_flag to an empty string and prints a logout message
    global user_flag
    user_flag = ''
    print('Logging out.')


def invalid_flag():
    #diagnostic function in case user_flag somehow becomes invalid
    print("user_flag invalid")
    quit()


def menu():
    #main menu
    while quit_flag == False:
        if user_flag == '':
            options_list = root_options
        elif user_flag in users:
            options_list = user_options
        else:
            invalid_flag()
        #evaluates who is using program and checks for valid user_flag

        list_options(options_list)
        selection = text_input('\nEnter your selection: ')
        select_menu(selection)
        #lists options, takes selection, and passes it to menu selector


def select_menu(selection):
    #intermediate function to pass selection to appropriate menu
    if user_flag == '':
        root_menu(selection)
    elif user_flag in users:
        user_menu(selection)
    else:
        invalid_flag()

def root_menu(selection):
    #evaluates selection if no user is logged in
    if selection == 'quit' or selection == 'q':
        quit()
    elif selection == 'login' or selection == 'l':
        username = login(users, users_file)
        global user_flag
        user_flag = username
        #sets user_flag after login is performed
    else:
        print('\nSelection invalid.')


def user_menu(selection):
    #evaluates selection if valid user is logged in
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