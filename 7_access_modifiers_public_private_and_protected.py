'''
Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.
'''
class Employee:
    def __init__(self,name,_salary,__ssn):
        self.name =  name #public variable
        self._salary = _salary #protected variable
        self.__ssn = __ssn #private variable

eply =  Employee('Ali',100,'23-45-5676')

# Easily Access public variable
print(eply.name)

# Accessible but should be treated as protected
print(eply._salary)
