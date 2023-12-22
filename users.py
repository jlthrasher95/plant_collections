"""This module stores classes for managing a dictionary of users
who each have a dictionary for user data.
The dictionary of users is stored in a JSON file.
"""


import json
import tool


class Session():
    def __init__(self, file_name):
        """This initializes the instance with a run flag,
        no active user, the target file's name, and the data
        from the target file if it exists. If no file exists,
        session data is set to an empty dictionary.
        """
        self.running = True
        self.user = None
        self.target_file = file_name
        try:
            with open(file_name) as file_object:
                users_dict = json.load(file_object)
        except FileNotFoundError:
            self.data = {}
        else:
            self.data = users_dict

    def save(self):
        """This method writes the session data to the target file."""
        with open(self.target_file, 'w') as file_object:
            json.dump(self.data, file_object)

    def add_user(self, username):
        """This method adds a user to session data with
        a blank dictionary for user data, then saves the session data.
        """
        self.data[username] = {}
        self.save()
        print("\nNew user created: " + username)
        print("Welcome, " + username.title() + ".")

    def login(self):
        """This method logs a user in, or else creates the user
        and then logs them in.
        """
        name = tool.caseless_input("\nEnter your name: ")
        if name in self.data:
            print("Welcome back, " + name.title() + "!")
            self.user = User(self, name)
        else:
            self.add_user(name)
            self.user = User(self, name)

    def logout(self):
        """This method clears the session user and prints a message."""
        self.user = None
        print('\nLogging out.')

    def end(self):
        """This method sets the session run flag to False and
        prints a message.
        """
        self.running = False
        print('\nExiting program.')


class User():
    def __init__(self, session, name):
        """This initializes the current user of a session by name
        and pulls their dictionary of user data for easy access.
        """
        self.session = session
        self.name = name
        self.data = session.data[name]

    def add_data(self, key, value):
        """This method adds a key-value pair to the user's data."""
        self.data[key] = value
        self.session.save()