from Enrollment import Enrollment

# Abstraction: Register provides a easy way for adding/removing students,
# teachers, courses and performing enrollments without exposing unnecassary details.

class Register:
    def __init__(self):
        self._students = {}     # student_id : student_object
        self._teachers = {}     # teacher_id : teacher_object
        self._courses = {}      # course_id : course_object
        self._enrollments = []  # list to store enrollment objects

    # method to add a student, teacher, and a course
    def add_student(self, student):                # creating abstraction 
        self._students[student.get_id()] = student # adding student object to the dictionary with student_id as key
    
    def add_teacher(self, teacher):                # creating abstraction
        self._teachers[teacher.get_id()] = teacher # adding teacher object to the dictionary with teacher_id as key

    def add_course(self, course):                  # creating abstraction
        self._courses[course.get_id()] = course    # adding course object to the dictionary with course_id as key


    # method to enroll a student to a course
    def enroll_student_to_course(self, student_id, course_id):
        if student_id in self._students and course_id in self._courses:
            enrollment = Enrollment(
                self._students[student_id],
                self._courses[course_id]
            )
            enrollment.enroll()
            self._enrollments.append(enrollment)
        else:
            print("Invalid Credentials,\nEither Student ID or Course ID is invalid.")

    # method to drop a student from a course
    def drop_student_from_course(self, student_id, course_id):
        if student_id in self._students and course_id in self._courses:
            for enrollment in self._enrollments:
                if (enrollment._student.get_id() == student_id and 
                    enrollment._course.get_id() == course_id):
                    enrollment.drop()
                    break
        else:
            print("Invalid Credentials,\nEither Student ID or Course ID is invalid.")

    
    # assigning a course to a teacher
    def assign_course_to_teacher(self, teacher_id, course_id):
        if teacher_id in self._teachers and course_id in self._courses:
            teacher = self._teachers[teacher_id]
            course = self._courses[course_id]
            # only assign if not already assigned
            if course_id not in teacher.get_courses():
                teacher.assign_course(course_id, prevent_print=True)
                print(f'Teacher "{teacher.get_name()}" is assigned Course "{course.get_name()}"')
            else:
                print(f'Teacher "{teacher.get_name()}" is already assigned Course "{course.get_name()}"')
        else:
            print("Invalid Credentials,\nEither Teacher ID or Course ID is invalid.")

    # removing a course from a teacher
    def remove_teacher_from_course(self, teacher_id, course_id):
        if teacher_id in self._teachers and course_id in self._courses:
            teacher = self._teachers[teacher_id]
            course = self._courses[course_id]
            # only remove if assigned
            if course_id in teacher.get_courses():
                teacher.remove_course(course_id, prevent_print=True)
                print(f'Teacher "{teacher.get_name()}" has been removed from Course "{course.get_name()}"')
            else:
                print(f'Course "{course.get_name()}" is not assigned to Teacher "{teacher.get_name()}"')

        else:
            print("Invalid Credentials,\nEither Teacher ID or Course ID is invalid.")

    
    # method to create getter for students, teachers, courses
    # this allows access to the encapsulated data
    def get_students(self):
        return self._students
    
    def get_teachers(self):
        return self._teachers
    
    def get_courses(self):
        return self._courses

    # method to remove a student and clean up related enrollments
    def remove_student(self, student_id):
        if student_id in self._students:
            # remove enrollments for this student
            self._enrollments = [e for e in self._enrollments if e._student.get_id() != student_id]
            del self._students[student_id]
            print("Student", student_id, "has been removed.")
        else:
            print("Invalid Student ID.")

    # method to remove a teacher and unassign its courses
    def remove_teacher(self, teacher_id):
        if teacher_id in self._teachers:
            del self._teachers[teacher_id]
            print("Teacher", teacher_id, "has been removed.")
        else:
            print("Invalid Teacher ID.")

    # method to remove a course and its references from students, teachers and enrollments
    def remove_course(self, course_id):
        if course_id in self._courses:
            for student in self._students.values():    # remove course id from all students
                if course_id in student.get_courses():
                    student.drop_courses(course_id)    # call student class drop method

            # remove course id from all teachers
            for teacher in self._teachers.values():
                if course_id in teacher.get_courses():
                    teacher.remove_course(course_id, prevent_print=True)   # calls teacher class' remove method

            # remove all enrollments related to this course id.
            self._enrollments = [e for e in self._enrollments if e._course.get_id() != course_id]
            del self._courses[course_id]
            print("Course", course_id, "has been removed.")
        else:
            print("Invalid Course ID.")
    