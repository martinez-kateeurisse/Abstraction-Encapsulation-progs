#Kate Eurisse Martinez_BSCPE 1-5_Abstraction & Encapsulation -Program 1

#(The Fan class).  Design a class named Fan to represent a fan. The class contains:
#Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
#A private int data field named speed that specifies the speed of the fan.
#A private bool data field named on that specifies whether the fan is on (the default is False).
#A private float data field named radius that specifies the radius of the fan.
#A private string data field named color that specifies the color of the fan.
#The accessor(getters)  and mutator(setters)  methods for all four data fields.
#A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
#Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

#Create a class
class Fan():
    #Create three constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #Add a constructor
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False ):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    #Create a private int data (fan speed)
    def fan_speed (self, speed):
        self.__speed = input(int("Specify Fan Speed: "))
    #Create a private bool data (fan power(on/off))
    def fan_power (self, on):
        self.__on = False 
    #Create a private float data (fan radius)
    def fan_radius (self, radius):
        self.__radius = input(float("Specify Fan Radius: "))
    #Create a private string data (fan color)
    def fan_color (self, color):
        self.__color = input(str("Specify Fan Color: "))
    #Create getter methods
    def get_speed(self):
        return self.__speed
    def get_power(self):
        return self.__on
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    #Create setter methods
    def set_age(self, speed):
        self.__speed = speed
    def set_power(self, on):
        self.__on = on
    def set_radius(self, radius):
        self.__radius = radius
    def set_color(self, color):
        self.__color = color

#Write a test program
    #Create two fan objects