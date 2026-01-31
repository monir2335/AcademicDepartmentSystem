from Register import Register
from database import DataController
from Menu import Menu 
from Auth import AuthenticationController

def main():
    
    #creating the controller for starting the menus
    register = Register()
    auth = AuthenticationController()

    # creating the database i.e. JSON file persistance
    database = DataController("data.json")
    # to load saved data
    database.load_data(register)

    # starting the menu 
    menu = Menu(register, database, auth)
    menu.start()

    # to save data before exiting program
    database.save_data(register)

    print("Data has been saved, Program Closing...")

if __name__ == "__main__":
    main()