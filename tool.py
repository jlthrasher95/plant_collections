'''tool.py is a module to store functions that I use regularly.'''


def text_input(prompt):
    '''
    "def" defines a new function. This function is named "text_input()",
    which will solicit input and convert it to a lowercase string.
    text_input() has one parameter, here called "prompt".
    '''

    reply = input(prompt)
    '''
    Here a new variable is created, called "reply".
    At the same time, Python's "input()" function is called to solicit user 
    input. The "prompt" parameter from text_input() is passed to the input()
    call as its only argument. This argument will be what the user is shown
    to request input.
    The variable "reply" is set to contain whatever value the input() function
    returns, which will be whatever the user enters.
    '''

    reply = str(reply.lower())
    '''
    Here the variable "reply" has its value set again, overwriting its
    original value.
    Python's str() function is called to convert a value to a string of text 
    in case it is not already one.
    The value passed as an argument to the str() call is the ".lower()"
    method of the "reply" variable. This converts all characters in the value
    of the reply variable to lowercase.
    '''

    return reply
'''
Now that the contents of "reply" have been converted to a lowercase string,
the reply variable is returned as the result of text_input(). This allows 
text_input() to be used like Python's input() function except that all user
input is automatically converted to a lowercase string.
'''


def list_options(list):
    print('\nThe following options are available:')
    for option in list:
        print('\t' + option.title())
