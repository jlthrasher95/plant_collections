'''This is a module to store functions that I use regularly.'''


vertical_space = '\n' * 12
dash_line = '-' * 64
program_running = True

    
def caseless_input(prompt):
    """This function prompts the user for input and converts it to
    lowercase.
    """
    reply = input(prompt)
    reply = reply.lower()
    return reply

def menu(options_dict):
    """This function takes a dictionary of options, presents them to the
    user, and then compares the user's selection to the available
    options. Keys that are one character long are not displayed,
    allowing for single-character shortcuts to be available but hidden.
    """
    print('\nThe following options are available:')
    for key in options_dict:
        if len(key) > 1:
            print('\t' + key.title())
    selection = caseless_input('\nEnter your selection: ')
    selection_validated = False
    for key in options_dict:
        if selection == key:
            options_dict[key]()
            selection_validated = True
    if not selection_validated:
        print('Invalid selection.')