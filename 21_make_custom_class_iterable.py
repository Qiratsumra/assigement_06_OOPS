# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
class Count_down:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <0:
            raise StopIteration #End of iteration
        value = self.current
        self.current -=1
        return value
    
for number in Count_down(10):
    print(number)