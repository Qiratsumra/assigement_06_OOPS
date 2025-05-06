# Create a class Person with a constructor that sets the name.
class Person:
    def __init__(self,name):
        self.name  = name
    def display_info(self):
        print(f'Name: {self.name}')
#  Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
class Treacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def display_info(self):
        super().display_info()
        print(f'Subject {self.subject}')
    
teacher1 = Treacher('Hira','English')
teacher1.display_info()