class Enrollment:

    # Encapsulation: stores student and course as encapsulated.
    # Abstraction: hides complexity of enrolling/dropping students
    # This handles student enrollments in courses

    def __init__(self, student, course):
        self._student = student   #encapsulated value
        self._course = course     #encapsulated value

    # method to enroll a student in a course
    def enroll(self, student=None, course=None, prevent_print=False):     
        # uses given value or else the stored ones
        s = student if student is not None else self._student
        c = course if course is not None else self._course

        # Refuse to enroll a different course via this Enrollment
        if c.get_id() != self._course.get_id():
            if not prevent_print:
                print("Cannot enroll: this Enrollment manages course", self._course.get_id())
            return

        if c.get_id() not in s.get_courses():                       
                s.enroll_courses(c.get_id(), prevent_print=True)
                if not prevent_print:
                    print("Student", s.get_name(), "has been enrolled in the course", c.get_name())
        else:
            if not prevent_print:
                print("Student", s.get_name(), "is already enrolled in the course", c.get_name())

    # method to remove a student from a course
    def drop(self, student=None, course=None, prevent_print=False):   
        # uses given value or else the stored ones
        s = student if student is not None else self._student
        c = course if course is not None else self._course

        # Refuse to drop a different course via this Enrollment
        if c.get_id() != self._course.get_id():
            if not prevent_print:
                print("Cannot drop: this Enrollment manages course", self._course.get_id())
            return

        if c.get_id() not in s.get_courses():
            if not prevent_print:
                print("Student", s.get_name(), "is not enrolled in the course", c.get_name())
        else:
                s.drop_courses(c.get_id(), prevent_print=True)
                if not prevent_print:
                    print("Student", s.get_name(), "has been removed/dropped from the course", c.get_name())