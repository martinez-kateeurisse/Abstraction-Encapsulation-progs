#This python file will include the methods that involves user-interface.

#Import fan class
from pet_class import Pet
from colorama import Back, Fore, Style 

#Create a class
class UserInterface():
    #Initialize object values to store the data 
    def __init__(self):
        self.pet = Pet(" "," "," ")
    
    #Asking for user inputs and setting values
    def pet_name (self):
        # Ask user to enter the name
        self.name = input(f"{Fore.LIGHTMAGENTA_EX}Please enter the pet's name: "+ Fore.RESET)
        #Set the name based on user's input
        self.pet.set_name(self.name)

    def pet_type (self):
        # Ask user to enter the type
        self.animal_type = input(f"{Fore.LIGHTMAGENTA_EX}Please enter the pet's animal type: "+ Fore.RESET)
        #Set the animal type based on user's input
        self.pet.set_animal_type(self.animal_type)

    def pet_age (self):
        # Ask user to enter the age
        self.age = float(input(f"{Fore.LIGHTMAGENTA_EX}Please enter pet's age: "+ Fore.RESET)) 
        #Set the nage base on user's input
        self.pet.set_age(self.age)

    #Displaying pet's details
    def pet_details(self):
        print(f"{Fore.LIGHTYELLOW_EX}\nPET DETAILS\n")
        print(f"{Fore.LIGHTCYAN_EX}Pet's Name: ", self.pet.get_name())
        print(f"{Fore.LIGHTCYAN_EX}Pet's Animal Type: ", self.pet.get_animal_type())
        print(f"{Fore.LIGHTCYAN_EX}Pet's Age: ", self.pet.get_age())       