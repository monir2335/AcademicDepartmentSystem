from Register import Register
from database import DataController
from Menu import Menu 
from Auth import AuthenticationController

def main():

    register = Register()                 # creating instances of Register class to manage students, teachers, courses
    auth = AuthenticationController()     # creating instance of AuthenticationController for login/signup

    database = DataController("data.json")   # creating thr database controller instance
    database.load_data(register)             # to load saved data from json.

    # starting the menu 
    menu = Menu(register, database, auth)    # creating instance of Menu class and calls Menu.
    menu.start()                             # starting menu

    database.save_data(register)             # to save data before exiting program

    print("Data has been saved, Program Closing...")

if __name__ == "__main__":
    main()