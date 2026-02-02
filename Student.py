from Person import Person

# Inheritance: Student inherits from Person 
# Encapsulation: uses internal attributes _enrolled_courses and _email to hide them
# Polymorphism: overrides display_info() defined as abstract in Person

class Student(Person):
    # student class is inheriting attributes from parent (Person) class.
    def __init__(self, name, person_id, email):
        super().__init__(name, person_id)  #initialize parent class attributes and merging with child class
        self._enrolled_courses = []   
        self._email = email      
    
    # method to enroll a course
    def enroll_courses(self, course_id, prevent_print=False):
        if course_id not in self._enrolled_courses:
            self._enrolled_courses.append(course_id)
            if not prevent_print:
                print("Student has been enrolled in the course", course_id)
        else:
            if not prevent_print:
                print("Student is Already Enrolled in course", course_id)

    # method to drop a course
    def drop_courses(self, course_id, prevent_print=False):
        if course_id not in self._enrolled_courses:
            if not prevent_print:
                print("The Student is not enrolled in course ID", course_id)
        else:
            self._enrolled_courses.remove(course_id)
            if not prevent_print:
                print("The Student has been dropped from course ID", course_id, ".")

    # getter for enrolled courses
    def get_courses(self):
        return self._enrolled_courses   #returns all enrolled courses
    
    # to display student information
    # this overrides the display_info in Person class, showing Polymorphism
    def display_info(self):
        print("\n| ======================================= |")
        print("| ========= STUDENT INFORMATION ========= |")
        print("| ======================================= |")
        print("| Student Name : ", self.get_name())
        print("| Student ID : ", self.get_id())
        print("| Student Email : ", self._email)
        print("| Enrolled Course : ", self._enrolled_courses if self._enrolled_courses else "None")
        print("| ======================================= |")

