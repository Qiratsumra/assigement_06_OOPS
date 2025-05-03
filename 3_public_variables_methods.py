# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    # Defined Public Variable
    def __init__(self,brand):
        self.brand = brand
    # Defined Public Class
    def start(self):
        print(f'{self.brand} has been started......')

car1 = Car('Toyota')
car1.start()
