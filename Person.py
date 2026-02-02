from abc import ABC, abstractmethod

class Person(ABC):

    # parent class for student and teacher class. It is an abstract class.

    def __init__(self, name, person_id):
        self._name = name               #encapsulated value
        self._person_id = person_id     #encapsulated value


    def get_name(self):
        return self._name 
    
    def get_id(self):
        return self._person_id

    # this is an abstract method, that will be implemented by its child classes
    @abstractmethod
    def display_info(self):            # POLYMORPHISM for student and teacher classes.
        pass

    @abstractmethod
    def get_courses(self):             # POLYMORPHISM for student and teacher classes.
        pass