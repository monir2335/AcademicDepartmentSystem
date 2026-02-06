import json
from Student import Student
from Teacher import Teacher
from Course import Course

class DataController:
    def __init__(self, filename = "data.json"):
        self._filename = filename 


    # ---------- SAVING DATA INTO JSON ----------------#
    # to save the data into json file
    def save_data(self, register): 
        data = {
            "students" : {},
            "teachers" : {},
            "courses" : {}
        }

        # to save student data
        for studentid, student in register.get_students().items():
            data["students"][studentid] = {
                "name" : student.get_name(),
                "email" : getattr(student, "_email",""),    # gets email attribute from student object
                "courses" : student.get_courses()
            }

        # to save teachers data
        for teacherid, teacher in register.get_teachers().items():
            data["teachers"][teacherid] = {
                "name" : teacher.get_name(),
                "email" : getattr(teacher, "_email",""),    # gets email attribute from teacher object
                "courses" : teacher.get_courses()
            }

        # to save courses data
        for courseid, course in register.get_courses().items():
            data["courses"][courseid] = {
                "name" : course.get_name(),                 
                "credits" : getattr(course, "_credits","")   # gets credits attribute from course object
            }

        # to open the json file
        with open(self._filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")


    # ---------- LOADING DATA FROM JSON ----------------#
    # to load the data which is saved in json file
    def load_data(self, register):  
        try:
            with open(self._filename, "r") as f:
                data = json.load(f)

            # to load student data
            for studentid, studentdata in data.get("students", {}).items():
                student = Student(studentdata["name"], studentid, studentdata.get("email", ""))
                for courseid in studentdata.get("courses", []):
                    student.enroll_courses(courseid, prevent_print=True)
                register.add_student(student)

            # to load teachers data
            for teacherid, teacherdata in data.get("teachers",{}).items():
                teacher = Teacher(teacherdata["name"], teacherid, teacherdata.get("email",""))
                for courseid in teacherdata.get("courses", []):
                    teacher.assign_course(courseid, prevent_print=True)
                register.add_teacher(teacher)

            # to load course data
            for courseid, coursedata in data.get("courses", {}).items():
                course = Course(courseid, coursedata["name"], coursedata.get("credits", 0))
                register.add_course(course)

            print("Data loaded successfully.")

        except FileNotFoundError:
            print("Data File Not Found.")
        except json.JSONDecodeError:
            print("Error reading data file.")