#Import fan class
from fan_class import Fan

#Create a class
class UserInterface():
    #Initialize object values
    def __init__(self):
        #Fan 1 status' values
        self.fan1 = Fan(Fan.FAST, 10, "yellow", True)
        #Fan 2 status' values
        self.fan2 = Fan(Fan.MEDIUM, 5, "blue", False)
    #Displaying Object 1/ Fan 1 status
    def obj1_display (self):
        print("\nFAN 1 - STATUS")
        print("Fan Speed:", self.fan1.get_speed()) # Fan 1 speed
        print("Fan Radius:", self.fan1.get_radius()) # Fan 1 radius
        print("Fan Color:", self.fan1.get_color()) # Fan 1 color
        if self.fan1.get_power() is True:
            print("Fan Power: On") #Fan 1 power status
        else:
            print("Fan Power: Off") #Fan 1 power status
    #Displaying Object 2/Fan 2 status
    def obj2_display (self):
        print("\nFAN 2 - STATUS")
        print("Fan Speed:", self.fan2.get_speed()) # Fan 2 speed
        print("Fan Radius:", self.fan2.get_radius()) # Fan 2 radius
        print("Fan Color:", self.fan2.get_color()) #Fan 2 color
        if self.fan2.get_power() is True:
            print("Fan Power: On") #Fan 2 power status
        else:
            print("Fan Power: Off") #Fan 2 power status