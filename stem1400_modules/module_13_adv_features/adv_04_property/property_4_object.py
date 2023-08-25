"""
module 13
built-in decorator @property

demo with property object
demo without @property
"""


# using property class
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    # temperature = property(get_temperature, set_temperature)

    # make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter(get_temperature)
    # assign fset
    temperature = temperature.setter(set_temperature)



# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

# new constraint implementation
try:
    # called setter
    human.temperature = -300
except ValueError as e:
    print(e)
