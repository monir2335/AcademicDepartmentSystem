from Student import Student
from Teacher import Teacher 
from Course import Course

# creating the Menu for User Interface

class Menu:
    def __init__(self, register, database, auth):
        self._register = register
        self._database = database
        self._auth = auth

    # starting the program, shows the admin login menu.
    # after successful login, comes the main menu 
    def start(self):
        while True:
            self.clear_screen()
            print("| ============ USER AUTHENTICATION ============ |")
            print("| 1.) LOG-IN                                    |")
            print("| 2.) SIGN-UP                                   |")
            print("| 0.) EXIT                                      |")
            print("| ============================================= |")

            ch = input("\nChoose an option (0-2) : ")
            if ch == "1":
                if self._auth and self._auth.log_in():
                    print("Login Successful!")
                    self.main_menu()      # showing main menu
                    break
                else:
                    print("Login failed.")
                    input("\nPress Enter to continue...")
            elif ch == "2":
                if self._auth:
                    self._auth.sign_up()  # creating new admin account
                    input("\nPress Enter to continue...")
                else:
                    print("Authentication controller not available.")
                    input("\nPress Enter to continue...")
            elif ch == "0":
                print("Exiting the program...")
                break
            else:
                input("Invalid Choice. Press Enter to continue...")


    # The Main Menu 
    def main_menu(self):
        while True:
            self.clear_screen()
            print("\n| =================================== |")
            print("| ============ MAIN MENU ============ |")
            print("| =================================== |")
            print("| 1.) Student Menu                    |")
            print("| 2.) Teacher Menu                    |")
            print("| 3.) Course Menu                     |")
            print("| 4.) Enrollment Menu                 |")
            print("| 5.) Reports                         |")
            print("| 0.) Log-Out                         |")
            print("| =================================== |")

            ch = input("\nChoose an option (0-5) : ")
            if ch == "1":
                self.student_menu()
            elif ch == "2":
                self.teacher_menu()
            elif ch == "3":
                self.course_menu()
            elif ch == "4":
                self.enrollment_menu()
            elif ch == "5":
                self.report_menu()
            elif ch == "0":
                print("Logging Out...")
                break
            else:
                input("Invalid Choice. Press Enter to continue...")


    # ============= The Student Menu ===========
    def student_menu(self):
        while True:
            self.clear_screen()
            print("\n| ============ STUDENT MENU ============ |")
            print("| 1.) Add Student                        |")
            print("| 2.) View Student                       |")
            print("| 3.) Delete Student                     |")
            print("| 0.) Back                               |")
            print("| ====================================== |")

            ch = input("\nChoose an option (0-3) : ")
            if ch == "1":
                studentid = input("\nEnter the Student ID : ")
                name = input("Enter the Student Name : ")
                email = input("Enter the Student Email : ")
                self._register.add_student(Student(name, studentid, email))
                print("Student has been added.")
                input("\nPress Enter to continue...")

            elif ch == "2":
                for stu in self._register.get_students().values():
                    stu.display_info()
                input("\nPress Enter to continue...")
            
            elif ch == "3":
                studentid = input("\nEnter the Student ID to delete : ")
                self._register.remove_student(studentid)
                input("\nPress Enter to continue...")

            elif ch == "0":
                break
            else:
                input("Invalid Choice. Press Enter to continue...")

            
    # ============ The Teachers Menu ===============
    def teacher_menu(self):
        while True:
            self.clear_screen()
            print("\n| ============ TEACHER MENU ============ |")
            print("| 1.) Add Teacher                        |")
            print("| 2.) View Teacher                       |")
            print("| 3.) Delete Teacher                     |")
            print("| 0.) Back                               |")
            print("| ====================================== |")

            ch = input("\nChoose an option (0-3) : ")
            if ch == "1":
                teacherid = input("\nEnter the Teacher ID : ")
                name = input("Enter the Teacher Name : ")
                email = input("Enter the Teacher Email : ")
                self._register.add_teacher(Teacher(name, teacherid, email))
                print("Teacher has been added.")
                input("\nPress Enter to continue...")

            elif ch == "2":
                for teach in self._register.get_teachers().values():
                    teach.display_info()
                input("\nPress Enter to continue...")
            
            elif ch == "3":
                teacherid = input("Enter the Teacher ID to delete : ")
                self._register.remove_teacher(teacherid)
                input("\nPress Enter to continue...")

            elif ch == "0":
                break
            else:
                input("Invalid Choice. Press Enter to continue...")


    # ============== The Course Menu =================
    def course_menu(self):
        while True:
            self.clear_screen()
            print("\n| ============ COURSE MENU ============ |")
            print("| 1.) Add a Course                      |")
            print("| 2.) View all Course                   |")
            print("| 3.) Delete a Course                   |")
            print("| 0.) Back                              |")
            print("| ===================================== |")

            ch = input("\nChoose an option (0-3) : ")
            if ch == "1":
                courseid = input("\nEnter the Course ID : ")
                name = input("Enter the Course Name : ")
                credits = int(input("Enter the Course Credits : "))
                self._register.add_course(Course(courseid, name, credits))
                print("Course has been added.")
                input("\nPress Enter to continue...")

            elif ch == "2":
                for cour in self._register.get_courses().values():
                    cour.display_course()
                input("\nPress Enter to continue...")
            
            elif ch == "3":
                courseid = input("Enter the Course ID to delete : ")
                self._register.remove_course(courseid)
                input("\nPress Enter to continue...")

            elif ch == "0":
                break
            else:
                input("Invalid Choice. Press Enter to continue...")


    # ============ The Enrollment Menu =================
    def enrollment_menu(self):
        while True:
            self.clear_screen()

            print("\n| ========== ENROLLMENT MENU ========== |")
            print("| 1.) Enroll a Student in a Course      |")
            print("| 2.) Drop a Student from a Course      |")
            print("| 3.) Assign a Teacher a Course         |")
            print("| 4.) Remove a Teacher from a Course    |")
            print("| 0.) Back                              |")
            print("| ===================================== |")

            ch = input("\nChoose an option (0-4) : ")
            if ch == "1":
                studentid = input("\nEnter the Student ID : ")
                courseid = input("Enter the Course ID : ")
                self._register.enroll_student_to_course(studentid, courseid)
                input("\nPress Enter to continue...")
            
            elif ch == "2":
                studentid = input("Enter the Student ID : ")
                courseid = input("Enter the Course ID : ")
                self._register.drop_student_from_course(studentid, courseid)
                input("\nPress Enter to continue...")

            elif ch == "3":
                teacherid = input("Enter the Teacher ID : ")
                courseid = input("Enter the Course ID : ")
                self._register.assign_course_to_teacher(teacherid, courseid)
                input("\nPress Enter to continue...")

            elif ch == "4":
                teacherid = input("Enter the Teacher ID : ")
                courseid = input("Enter the Course ID : ")
                self._register.remove_teacher_from_course(teacherid, courseid)
                input("\nPress Enter to continue...")
            
            elif ch == "0":
                break
            else:
                input("Invalid Choice. Press Enter to continue...")


    # ==================== REPORT MENU ================
    def report_menu(self):
        self.clear_screen()
        print("\n| ============= REPORTS ============= |")


        print("\n Students : ")
        for stu in self._register.get_students().values():
            stu.display_info()

        print("\n\n Teachers : ")
        for teach in self._register.get_teachers().values():
            teach.display_info()

        print("\n\n Courses : ")
        for cour in self._register.get_courses().values():
            cour.display_course()
        input("\nPress Enter to continue...")
        
    def clear_screen(self):
        print("\n"*100) # simple way to clear the screen
