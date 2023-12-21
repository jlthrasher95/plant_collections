"""This module stores classes for managing a dictionary of users
who each have a dictionary for user data.
The dictionary of users is stored in a JSON file.
"""


import json
import tool


class Session():
    def __init__(self, file_name):
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
        with open(self.target_file, 'w') as file_object:
            json.dump(self.data, file_object)

    def add_user(self, username):
        self.data[username] = {}
        self.save()
        print("\nNew user created: " + username)
        print("Welcome, " + username.title() + ".")

    def login(self):
        name = tool.text_input("\nEnter your name: ")
        if name in self.data:
            print("Welcome back, " + name.title() + "!")
            self.user = User(self, name)
        else:
            self.add_user(name)
            self.user = User(self, name)

    def logout(self):
        self.user = None
        print('\nLogging out.')

    def end(self):
        self.running = False
        print('\nExiting program.')


class User():
    def __init__(self, session, name):
        self.session = session
        self.name = name
        self.data = session.data[name]

    def add_data(self, key, value):
        self.data[key] = value
        self.session.save()