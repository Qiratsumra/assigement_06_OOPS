# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,id,name,role):
        self.id = id
        self.name = name
        self.role = role

    def empolyee_details(self):
        print(f'Name: {self.name}')
        print(f'ID: {self.id}')

class Department:
    def __init__(self,dept,empolyee):
        self.dept = dept
        self.empolyee = empolyee

    def display_department_details(self):
        print(f'Department: {self.dept} ')
        self.empolyee.empolyee_details()

emp = Employee(12,'Ali','Software Developer')
dept = Department('Software Developer',emp)
dept.display_department_details()