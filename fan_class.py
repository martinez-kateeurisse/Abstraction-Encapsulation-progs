#Kate Eurisse Martinez_BSCPE 1-5_Abstraction & Encapsulation -Program 1

#General program instructions can be seen in the readme file.

#Create a class
class Fan():
    #Create three constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    #Add a constructor
    def __init__(self, speed = 1, radius = 5, color = "blue", on = False ):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    #Create a private int data (fan speed)
    #Can be used when modified into a user-interactive program
    def fan_speed (self, speed):
        self.__speed = input(int("Specify Fan Speed: "))
    #Create a private bool data (fan power(on/off))
    def fan_power (self):
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