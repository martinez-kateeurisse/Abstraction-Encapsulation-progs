#This python file will serve as the main file that will be run.

#A python program that lets the user input the pet's name, type ,and age. Then, displaying them through certain methods.

#Import classes
from pet_class import Pet
from pet_ui import UserInterface
from progs_design import ProgramDesign 

#Initialize class
ui = UserInterface()
design = ProgramDesign()

#Program Introduction
design.pet_header()
design.greetings()
design.loading_bar()

#Setting pet's name through user's input
ui.pet_name()
#Setting pet's animal type through user's input
ui.pet_type()
#Setting pet's age through user's input
ui.pet_age()
 
#Loading bar
design.details_loading()

#Displaying pet's details (normal execution)
ui.pet_details()