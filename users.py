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


    def user_input(self, prompt):
        """This method performs a quit check on user input and returns
        the input.
        """
        reply = tool.caseless_input(prompt)
        self.quit_check(reply)
        return reply


    def add_user(self, username):
        """This method adds a user to session data with
        a blank dictionary for user data, then saves the session data.
        """
        self.data[username] = {}
        self.save()
        print("\nNew user created: " + username)
        print("Welcome, " + username.title() + ". You may now log in.")


    def sign_up(self):
        """This allows a new user to be created, provided that the name
        is not taken.
        """
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Signup canceled.")
                    break
                elif name in self.data:
                    print("That username is already taken.")
                else:
                    self.add_user(name)
                    break
            name = self.user_input("\nEnter your name, or 'back' to go back: ")


    def add_to_user(self, key, value):
        """This method sets a key-value pair in the user's data."""
        self.user_data[key] = value
        self.save()


    def login(self, name):
        print("Welcome, " + name.title() + "!")
        self.user = name
        self.user_data = self.data[name]


    def sign_in(self):
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Signin canceled.")
                    break
                elif name in self.data:
                    self.login(name)
                    break
                else:
                    print("Username not found.")
            name = self.user_input("\nEnter your name, or 'back' to go back: ")
            

    def logout(self):
        """This method clears the session user and prints a message."""
        self.user = None
        self.user_data = None
        print('\nLogging out.')
