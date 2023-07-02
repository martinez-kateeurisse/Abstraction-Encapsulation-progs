#This python file will include the methods that involves user-interface.

#Import fan class
from pet_class import Pet
from colorama import Back, Fore, Style 
from pyfiglet import Figlet

#Create a class
class UserInterface():
    #Initialize object values to store the data 
    def __init__(self):
        self.pet = Pet(" "," "," ")
    
    #Program brief instruction
    def prog_instructions(self):
        print("\nThis program will ask for your pet's name, animal type, and age. Then, display the given details\n")

    #Asking for user inputs and setting values
    def pet_name (self):
        # Ask user to enter the name
        self.name = input(f"{Fore.LIGHTMAGENTA_EX}\nPlease enter the pet's name: "+ Fore.RESET)
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
        header = Figlet(font='bubble')
        title = Figlet(font='digital')
        info = Figlet(font = 'larry3d')
        pet_details = header.renderText("PET DETAILS")

        name_title = title.renderText("Pet's Name: ")
        name_output = info.renderText(self.pet.get_name())
        type_title = title.renderText("Pet's Animal Type: ")
        type_output = info.renderText(self.pet.get_animal_type())
        age_title = title.renderText("Pet's Age: ") 
        age_output = info.renderText(str(self.pet.get_age()))

        # Print the ASCII art
        print(Fore.LIGHTYELLOW_EX + pet_details)
        print(Fore.LIGHTCYAN_EX + name_title)
        print(Fore.LIGHTRED_EX + name_output)
        print(Fore.LIGHTCYAN_EX + type_title)
        print(Fore.LIGHTRED_EX + type_output)
        print(Fore.LIGHTCYAN_EX + age_title) 
        print(Fore.LIGHTRED_EX + age_output)

    #Displaying output when executing in pygame(can be used if modified)
    def pet_detail(self):
        details = "\nPET DETAILS\n"
        details += f"Pet's Name: {self.pet.get_name()}\n"
        details += f"Pet's Animal Type: {self.pet.get_animal_type()}\n"
        details += f"Pet's Age: {self.pet.get_age()}"
        return details