"""This module stores a class for managing a program session which
can read to and write from a specified JSON file.
"""


import json
import tool


class Session():
    def __init__(self, file_name):
        """This initializes the instance with a dictionary of data from
        a file if it exists, a run flag, and no key selected.
        """
        self.running = True
        self.key = None
        self.key_data = None
        self.target_file = file_name
        try:
            with open(file_name) as file_object:
                data_dict = json.load(file_object)
        except FileNotFoundError:
            self.data = {}
        else:
            self.data = data_dict


    def save(self):
        """This method writes the session data to the target file."""
        with open(self.target_file, 'w') as file_object:
            json.dump(self.data, file_object, indent=4, sort_keys=True)
            

    def end(self):
        """This method sets the session run flag to False and
        prints a message.
        """
        self.running = False
        print('\nExiting program.')


    def quit_check(self, string):
        """This method checks a string for quit conditions."""
        if string in ('q', 'quit'):
            self.end()


    def key_input(self, prompt):
        reply = tool.caseless_input(prompt)
        self.quit_check(reply)
        return reply