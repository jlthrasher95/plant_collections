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


    def login(self, name):
        """This method selects a current user and loads their data."""
        self.user = name
        self.user_data = self.data[name]
        print("Welcome, " + name.title() + "! You are logged in.")


    def logout(self):
        """This method clears the session user and prints a message."""
        self.user = None
        self.user_data = None
        print('\nLogging out.')


    def add_user(self, name):
        """This method adds a user to session data with
        a blank dictionary for user data, then saves the session data.
        """
        self.data[name] = {}
        self.save()
        print("\nNew user created: " + name)


    def delete_user(self, name):
        """This method deletes a user from the database."""
        del self.data[name]
        self.save()
        print("User " + name + " deleted.")


    def add_to_user(self, key, value):
        """This method sets a key-value pair in the user's data."""
        self.user_data[key] = value
        self.save()


    def delete_from_user(self, name):
        """This method deletes a key-value pair from the user's data."""
        del self.user_data[name]
        self.save()

    
    def change_name_data(self, old_name, new_name):
        """This method copies a user's data into a new username and
        deletes the old user.
        """
        self.data[new_name] = self.data[old_name]
        del self.data[old_name]
        self.save()
        print("Username changed.")


    def user_input(self, prompt):
        """This method performs a quit check on user input and returns
        the input.
        """
        reply = tool.caseless_input(prompt)
        self.quit_check(reply)
        return reply
    
    
    def view_users(self):
        """This method lists all users."""
        print("List of users:")
        for user in self.data:
            print("\t" + user.title())


    def sign_up(self):
        """This method allows a new user to be created, provided that
        the name is not taken.
        """
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Signup canceled.")
                    return False
                elif name in self.data:
                    print("That username is already taken.")
                else:
                    self.add_user(name)
                    self.login(name)
                    return True
            name = self.user_input("\nEnter your name, or 'back' to go back: ")


    def remove_user(self):
        """This method prompts the user for a name to be removed."""
        prompt = "\nEnter the username to remove, or 'back' to go back: "
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Removal canceled.")
                    return False
                elif name in self.data:
                    self.delete_user(name)
                    return True
                else:
                    print("The user " + name + " does not exist.")
            name = self.user_input(prompt)


    def sign_in(self):
        """This method prompts the user for a username and logs them in
        if the user exists.
        """
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Signin canceled.")
                    return False
                elif name in self.data:
                    self.login(name)
                    return True
                else:
                    print("Username not found.")
            name = self.user_input("\nEnter your name, or 'back' to go back: ")


    def change_name(self):
        """This method lets a user change their name."""
        prompt = "\nEnter your new name, or 'back' to go back: "
        name = None
        while self.running:
            if name:
                if name in ('back', 'b'):
                    print("Name change canceled.")
                    return False
                elif name in self.data:
                    print("That username is already taken.")
                else:
                    self.change_name_data(self.user, name)
                    self.login(name)
                    return True
            name = self.user_input(prompt)
            