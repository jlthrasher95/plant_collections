"""This module stores a class for managing a dictionary of users
who each have a dictionary for user data.
The dictionary of users is stored in a JSON file.
"""


import tool, persistent


class Session(persistent.Session):
    def __init__(self, file_name):
        """This initializes the instance with self.user and
        self.user_data aliased to self.key and self.key_data.
        """
        super().__init__(file_name)
        self.user = self.key
        self.user_data = self.key_data


    def add_user(self, username):
        """This method adds a user to session data with
        a blank dictionary for user data, then saves the session data.
        """
        self.data[username] = {}
        self.save()
        print("\nNew user created: " + username)
        print("Welcome, " + username.title() + ". You may now log in.")


    def signup(self):
        """This allows a new user to be created, provided that the name
        is not taken.
        """
        name = None
        while self.running:
            if name:
                if name in self.data:
                    print("That username is already taken.")
                else:
                    self.add_user(name)
                    break
            name = self.key_input("\nEnter your name: ")



    def add_to_user(self, key, value):
        """This method sets a key-value pair in the user's data."""
        self.user_data[key] = value
        self.save()


    def login(self):
        """This function will select a user by name and load their data,
        or else will reprompt for input until either a valid user or a
        quit string is entered.
        """
        name = None
        while self.running:
            if name:
                if name in self.data:
                    print("Welcome back, " + name.title() + "!")
                    self.user = name
                    self.user_data = self.data[name]
                    break
                else:
                    print("Username not found.")
            name = self.key_input("\nEnter your name: ")
            

    def logout(self):
        """This method clears the session user and prints a message."""
        self.user = None
        self.user_data = None
        print('\nLogging out.')
