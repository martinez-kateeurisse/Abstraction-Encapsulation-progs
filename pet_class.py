#Kate Eurisse Martinez_BSCPE 1-5_Abstraction & Encapsulation -Program 3

#Program Instructions
#Write a class named Pet, which should have the following data attributes:
#• _ _name (for the name of a pet)
#• _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
#• _ _age (for the pet’s age)

#The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
#• set_name()
#This method assigns a value to the _ _name field.
#• set_animal_type()
#This method assigns a value to the _ _animal_type field.
#• set_age()
#This method assigns a value to the _ _age field.
#• get_name()
#This method returns the value of the _ _ name field.
#• get_animal_type()
#This method returns the value of the _ _animal_type field.
#• get_age()
#This method returns the value of the _ _age field.

#Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.


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