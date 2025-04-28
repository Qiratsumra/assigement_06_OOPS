# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # keep track of the number of objects created
    def __init__(self):
        Counter.count += 1
        print(f"Object created. Current count: {Counter.count}") # count the number of the is created

    @classmethod # converts the function into a class method
    def displayer_counter(cls):
        print(f"Total objects created: {cls.count}")


count1 = Counter()
count2 = Counter()
count3 = Counter()
count4 = Counter()
count5 = Counter()
count6 = Counter()
count7 = Counter()