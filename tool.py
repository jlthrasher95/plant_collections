'''tool.py is a module to store functions that I use regularly.'''

vertical_space = '\n\n\n\n\n\n\n\n\n\n\n\n'
dash_line = '----------------------------------------------------------------'
run_flag = True


def quit():
    global run_flag
    run_flag = False
    print('\nExiting program.')
    
def text_input(prompt):
    reply = input(prompt)
    reply = str(reply.lower())
    return reply

def menu(list):
    print('\nThe following options are available:')
    for option in list:
        print('\t' + option.title())
    selection = text_input('\nEnter your selection: ')
    return selection
