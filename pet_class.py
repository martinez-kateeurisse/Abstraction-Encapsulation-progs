#Kate Eurisse Martinez_BSCPE 1-5_Abstraction & Encapsulation -Program 3

#This python file includes the pet class which have the needed methods to run the program (test_pet).
#General instructions of the program can be seen in the readme file.

#Create a class
class Pet():
#Add a constructor
    def __init__ (self, name, animal_type, age):
    #Create data attributes
        self.__name = name  #Pet name
        self.__animal_type = animal_type  #Animal type
        self.__age = age    #Pet age

#Create methods
    #Setters
    def set_name(self, name): #Name
        self.__name = name
    def set_animal_type(self, animal_type): #Animal type
        self.__animal_type = animal_type  
    def set_age(self, age): #Age
        self.__age = age

    #Getters  
    def get_name(self): #Name
        return self.__name
    def get_animal_type(self):  #Animal type
        return self.__animal_type
    def get_age(self):  #Age
        return self.__age