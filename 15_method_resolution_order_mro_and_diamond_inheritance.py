'''
Create four classes:
A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.
Create an object of D and call show() to observe MRO.
'''
class A:
    @staticmethod
    def show():
        print('Show from class A')
class B(A):
    @staticmethod
    def show():
        print('Show from class B')
class C(A):
    @staticmethod
    def show():
        print('Show from class C')

class D(B,C):
    pass
d = D()
d.show()
print(D.__mro__)