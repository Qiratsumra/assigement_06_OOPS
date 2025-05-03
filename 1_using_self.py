# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    name :str
    mark: int

    def __init__(self,name,marks):
        self.name = name
        self.mark =  marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.mark}")


name  =  input('Enter your name: ')
marks =  int(input('Enter your marks: '))
student = Student(name,marks)
student.display()