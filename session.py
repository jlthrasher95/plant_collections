import json
import tool

class Session():
    def __init__(self, file_name):
        try:
            with open(file_name) as file_object:
                users_dict = json.load(file_object)
        except FileNotFoundError:
            self.database = {}
        else:
            self.database = users_dict

        self.running = True
        self.user = ''
        self.user_data = {}
        self.target_file = file_name

    def save(self):
        with open(self.target_file, 'w') as file_object:
            json.dump(self.database, file_object)

    def add_user(self, username):
        self.database[username] = {}
        self.save()
        print("\nNew user created: " + username)
        print("Welcome, " + username.title() + ".")

    def login(self):
        self.user = tool.text_input("\nEnter your name: ")
        if self.user in self.database:
            print("Welcome back, " + self.user.title() + "!")
            self.user_data = self.database[self.user]
        else:
            self.add_user(self.user)
            self.user_data = self.database[self.user]

    def logout(self):
        self.user = ''
        self.user_data = {}
        print('\nLogging out.')

    def end(self):
        self.running = False
        print('\nExiting program.')
