from Person import Person

# Inheritance: Teacher inherits from Person
# Encapsulation: keeps _teaching_courses and _email private
# Polymorphism: overrides display_info() from Person

class Teacher(Person):
    # teacher class inherits attributes from Person (parent) class
    def __init__(self, name, person_id, email):
        super().__init__(name, person_id)  # initialize parent class attributes and merging with teacher class.
        self._teaching_courses = []
        self._email = email         

    # method to assign a course to a teacher if not assigned
    def assign_course(self, course_id, prevent_print=False):
        if course_id not in self._teaching_courses:
            self._teaching_courses.append(course_id)
            if not prevent_print:
                print("The Course", course_id, "has been assigned to teacher", self.get_name())
        else:
            if not prevent_print:
                print("The Course", course_id, "is already assigned to teacher", self.get_name())

    # method to remove a course from a teacher's assigned courses
    def remove_course(self, course_id, prevent_print=False):
        if course_id not in self._teaching_courses:
            if not prevent_print:
                print("The Course", course_id, "is not assigned to the teacher", self.get_name(), ".")
        else:
            self._teaching_courses.remove(course_id)
            if not prevent_print:
                print("The Course", course_id, "has been removed from teacher", self.get_name())
    
    # to get all teaching courses
    def get_courses(self):
        return self._teaching_courses # this returns all assigned courses.
    
    # to display teacher information,
    # this overrides the display_info in Person class, showing Polymorphism
    def display_info(self):
        print("\n| ======================================= |")
        print("| ========= TEACHER INFORMATION ========= |")
        print("| ======================================= |")
        print("| Teacher Name: ", self.get_name())
        print("| Teacher ID: ", self.get_id())
        print("| Teacher Email: ", self._email)
        print("| Teaching Courses: ", self._teaching_courses if self._teaching_courses else "None")
        print("| ======================================= |")


