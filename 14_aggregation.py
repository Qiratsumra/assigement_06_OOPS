# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,id,name,role):
        self.id = id
        self.name = name
        self.role = role
    def emplyee_details(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')
        print(f'ID: {self.role}')

class Department:
    def __init__(self,dept,emplyee_details):
        self.dept = dept
        self.emplyee_details = emplyee_details

    def display_department_details(self):
        print(f'{self.dept} {self.emplyee_details}')
        self.emplyee_details()

emp = Employee(12,'Ali','Software Developer')
dept = Department('Software Developer',emp)
dept.display_department_details()