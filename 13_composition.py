# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
class Engine :
    def __init__(self,name):
        self.name =  name

    @staticmethod
    def start_engine():
        print('Engine is start........')
class Car:
    def __init__(self,brand,engine:Engine):
        self.brand = brand
        self.engine = engine
    def start(self):
        print(f'{self.brand} \n{self.engine}')


car = Car('Tesla','Internal Combustion Engines ')
car.start()