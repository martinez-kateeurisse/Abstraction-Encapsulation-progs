#This python file will include the methods that involves user-interface.

#Import fan class
from pet_class import Pet

#Create a class
class UserInterface():
    #Initialize object values to store the data 
    def __init__(self):
        self.pet = Pet(" "," "," ")
    
    #Asking for user inputs and setting values
    def pet_name (self):
        # Ask user to enter the name
        self.name = input("Please enter the pet's name: ")
        #Set the name based on user's input
        self.pet.set_name(self.name)

    def pet_type (self):
        # Ask user to enter the type
        self.animal_type = input("Please enter the pet's animal type: ")
        #Set the animal type based on user's input
        self.pet.set_animal_type(self.animal_type)

    def pet_age (self):
        # Ask user to enter the age
        self.age = float(input("Please enter pet's age: ")) 
        #Set the nage base on user's input
        self.pet.set_age(self.age)

    #Displaying pet's details
    def pet_details(self):
        print("PET DETAILS")
        print("Pet's Name: ", self.pet.get_name())
        print("Pet's Animal Type: ", self.pet.get_animal_type())
        print("Pet's Age: ", self.pet.get_age())      