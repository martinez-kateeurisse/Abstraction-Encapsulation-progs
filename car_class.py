#Kate Eurisse Martinez_BSCPE 1-5_Abstraction & Encapsulation - Program 2

#A python program that include a car class with three attributes (year model, make and speed) and 3 methods (accelerate, brake, get_speed).
#General instructions for this program can be seen in the readme file.

#Create a Car Class
class Car():
    #Add a constructor
    def __init__ (self, year_model, make, speed=0):
    #Create data attributes
        self.__year_model = year_model #Year model
        self.__make = make  #Make of the car
        self.__speed = speed  #Speed

    #Create accelerate method
    def accelerate(self):
        self.__speed += 5
    
    #Create break method
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    
    #Return the speed 
    def get_speed(self):
        return self.__speed