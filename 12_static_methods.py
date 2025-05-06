# Create a class TemperatureConverter with a static method celsius\_to\_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp1 = TemperatureConverter()
c_t_f=temp1.celsius_to_fahrenheit(100)
print(c_t_f)