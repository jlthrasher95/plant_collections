'''This is a module to store objects that I use regularly.'''


vertical_space = '\n' * 12
dash_line = '-' * 64

    
def caseless_input(prompt):
    """This function returns all-lowercase input."""
    reply = input(prompt)
    reply = reply.lower()
    return reply


def menu(options_dict):
    """This function prints a formatted list of options from
    a dictionary, then takes the user's selection and
    passes it to run_selection().
    """
    print('\nThe following options are available:')
    for key_tuple in options_dict:
        print('\t' + key_tuple[0].title())
    selection = caseless_input('\nEnter your selection: ')
    run_selection(selection, options_dict)


def run_selection(selection, options_dict):
    """This function compares a user's selection against a dictionary of
    options and runs the corresponding function, or else notifies the
    user that the selection was invalid.
    """
    for key_tuple in options_dict.keys():
        for subkey in key_tuple:
            if selection == subkey:
                options_dict[key_tuple]()
                return True
    print('Invalid selection.')
    return False


def list_for_writelines(list):
    """This function formats a list for writelines()."""
    lines = []
    for item in list:
        lines.append(str(item) + '\n')
    return lines


def list_to_textfile(tuples, filename):
    """This function writes a list to a text file."""
    str_tuples = list_for_writelines(tuples)
    with open(filename, 'w') as file_object:
        file_object.writelines(str_tuples)


def add_to_file(value, filename):
    """This function appends a value to a text file as a new line."""
    with open(filename, 'a') as file_object:
        file_object.write(str(value) + '\n')


def unstring_ints(strings):
    """This function converts a list of string-integers to integers."""
    ints = []
    for str_int in strings:
        ints.append(int(str_int))
    return ints


def unstring_int_tuples(strings):
    """This function converts integer-tuples stored as strings into
    tuples of integers.
    """
    tuples = []
    for str_tuple in strings:
        strs_list = str_tuple[1:-2].split(", ")
        tuple_ = tuple(unstring_ints(strs_list))
        tuples.append(tuple_)
    return tuples


def int_tuples_from_textfile(filename):
    """This function reads a list of tuples from a text file."""
    try:
        with open(filename, 'r') as file_object:
            tuples = unstring_int_tuples(file_object.readlines())
    except FileNotFoundError:
        tuples = [(0, 0),]
        print('File not found.')
    return tuples