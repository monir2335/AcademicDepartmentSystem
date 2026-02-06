class Course:
    
    # Encapsulation: course details are private
    # Abstraction: provides easy way to get (get_id, get_name) hiding internal process

    def __init__(self, course_id, course_name, credits):
        self._course_id = course_id        # encapsulated value
        self._course_name = course_name    # encapsulated value
        self._credits = credits            # encapsulated value

    # to return the Course ID
    def get_id(self):                      
        return self._course_id

    # to return the course name
    def get_name(self):                  
        return self._course_name
    
    # to display all course information
    def display_course(self):
        print("\n| ====================================== |")
        print("| ========= COURSE INFORMATION ========= |")
        print("| Course ID: ", self._course_id)
        print("| Course Name: ", self._course_name)
        print("| Course Credits: ", self._credits)
        print("| ====================================== |")
