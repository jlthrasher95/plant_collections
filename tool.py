'''This is a module to store functions that I use regularly.'''


vertical_space = '\n' * 12
dash_line = '-' * 64
program_running = True

    
def text_input(prompt):
    """This prompts the user for input and converts it to a lowercase
    string.
    """
    reply = input(prompt)
    reply = str(reply.lower())
    return reply

def menu(list):
    """This offers a list of options to the user and returns their
    selection.
    """
    print('\nThe following options are available:')
    for option in list:
        print('\t' + option.title())
    selection = text_input('\nEnter your selection: ')
    return selection
