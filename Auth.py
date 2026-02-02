import json
import os


class AuthenticationController:
    def __init__(self, filename="admin.json"):
        self.filename = filename  # creating and storing data in json file
        self._load_admin_credentials()  # loaading admin credentials from json file

    def _load_admin_credentials(self):
        if os.path.exists(self.filename):  # checking if the file exists
            with open(self.filename, "r") as f:
                self.admin_credentials = json.load(f)  # loading the credential from json file
        else:
            self.admin_credentials = {}  # if file does not exist, create an empty dictionary
            
            self._save_admin_credentials()  # if file does not exist create a new one

    def _save_admin_credentials(self):  # saving admin data into json file
        with open(self.filename, "w") as f:
            json.dump(self.admin_credentials, f, indent=4)

    # --------- SIGN UP ----------------
    def sign_up(self):
        print("\n| ====================================== |")
        print("| ============ USER SIGN UP ============ |")
        print("| ====================================== |")

        username = input("Enter a new username : ")

        if username in self.admin_credentials:  # check if username exists
            print("Error! Username already exists.")
            return False

        password = input("Enter a new password : ")  # get password from admin

        # storing new username and password
        self.admin_credentials[username] = password

        self._save_admin_credentials()  # saving new admin credentials to json file

        print("New Admin Account has been created successfully.")
        return True

    # --------- LOGIN ---------------
    def log_in(self):
        print("\n| ====================================== |")
        print("| ============ USER LOG IN ============= |")
        ("| ====================================== |")
        username = input("\nEnter a username : ")

        # check if username exists BEFORE asking for password
        if username not in self.admin_credentials:
            print("Error! Invalid Username.")
            return False

        password = input("Enter a password : ")

        if password != self.admin_credentials[username]:
            print("Error! Incorrect Password.")
            return False
        else:
            print("\nWELCOME,", username)
            return True
