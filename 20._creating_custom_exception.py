# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
# define custom exception
class InvalidAgeError(Exception):
    def __init__(self,age):
        super.__init__(age)
def check_age(age):
    if age<=18:
        print('Access granted')
    else:
         raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")
    
try:
    user_age = 18
    check_age(user_age)
except IndentationError as e:
    print(f'Access denied {e}')