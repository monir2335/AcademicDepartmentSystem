class Enrollment:
    # Encapsulation: stores student and course objects internally
    # Abstraction: provides a clear interface for enrolling/dropping without the caller manipulating internals
    # This handles student enrollments in courses
    def __init__(self, student, course):
        self._student = student   #encapsulated value
        self._course = course     #encapsulated value

    # method to enroll a student in a course
    def enroll(self, student=None, course=None, prevent_print=False):
        # Use provided student/course or fall back to the ones stored on this Enrollment
        s = student if student is not None else self._student
        c = course if course is not None else self._course

        # Don't allow enrolling via this Enrollment for a different course
        if c.get_id() != self._course.get_id():
            if not prevent_print:
                print("Cannot enroll: this Enrollment manages course", self._course.get_id())
            return

        if c.get_id() not in s.get_courses():
                # prevent the Student object from printing; Enrollment prints a single message
                s.enroll_courses(c.get_id(), prevent_print=True)
                if not prevent_print:
                    print("Student", s.get_name(), "has been enrolled in the course", c.get_name())
        else:
            if not prevent_print:
                print("Student", s.get_name(), "is already enrolled in the course", c.get_name())

    # method to remove a student from a course
    def drop(self, student=None, course=None, prevent_print=False):
        # Use provided student/course or fall back to the ones stored on this Enrollment
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
                # prevent the Student object from printing; Enrollment prints a single message
                s.drop_courses(c.get_id(), prevent_print=True)
                if not prevent_print:
                    print("Student", s.get_name(), "has been removed/dropped from the course", c.get_name())

    # method to display enrollment information
    def display_enrollment(self):
        print("="*40)
        print("Enrollment Information:")
        print("Student Name: ", self._student.get_name())
        print("Student ID: ", self._student.get_id())
        print("Course Name: ", self._course.get_name())
        print("Course ID: ", self._course.get_id())
        # show whether the student is currently enrolled in this course
        enrolled = self._course.get_id() in self._student.get_courses()
        print("Enrollment Status:", "Enrolled" if enrolled else "Not enrolled")
        print("="*40)

