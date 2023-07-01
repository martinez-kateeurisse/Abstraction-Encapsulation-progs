#Write a test program

#Import fan class
from fan_class import Fan

#Create two fan objects
fan1 = Fan(Fan.FAST, 10, "yellow", True)
print("FAN 1 - STATUS")
print("Fan Speed:", fan1.get_speed())
print("Fan Radius:", fan1.get_radius())
print("Fan Color:", fan1.get_color())
print("Fan Power (On):", fan1.get_power())

fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

