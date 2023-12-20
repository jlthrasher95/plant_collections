'''This module holds functions that I use regularly.'''


vertical_space = '\n' * 12
dash_line = '-' * 64
program_running = True


def end_run():
    """This function sets program_running to false and
    prints a message.
    """
    global program_running
    program_running = False
    print('\nExiting program.')


def caseless_input(prompt):
    """This function prompts the user for input and
    converts it to lowercase.
    """
    reply = input(prompt)
    reply = reply.lower()
    return reply


def menu(list):
    """This function offers a list of options to the user and
    returns their selection.
    """
    print('\nThe following options are available:')
    for option in list:
        print('\t' + option.title())
    selection = caseless_input('\nEnter your selection: ')
    return selection
