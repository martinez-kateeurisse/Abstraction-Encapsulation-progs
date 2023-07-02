#This python file will serve as the main file that will be run.

#A python program that lets the user input the pet's name, type ,and age. Then, displaying them through certain methods.

#Import classes
from pet_class import Pet
from pet_ui import UserInterface
from progs_design import ProgramDesign 

#Initialize class
ui = UserInterface()
design = ProgramDesign()

#Program header
design.pet_header()
design.loading_bar()

#Setting pet's name through user's input
ui.pet_name()
#Setting pet's animal type through user's input
ui.pet_type()
#Setting pet's age through user's input
ui.pet_age()

#Displaying pet's details (normal execution)
#ui.pet_details()

#Executing through pygame
# Import modules
import pygame
from pygame.locals import *
import sys

# Initialize pygame
pygame.init()

# Initialize window display format (dimensions)
window_width = 550
window_height = 320
display = pygame.display.set_mode((window_width, window_height))

# Set text formats (font and color)
output_font = pygame.font.Font("awesome.ttf", 30)

# Create an instance of the UserInterface class
ui = UserInterface()

# Run the program in pygame
# Use a loop to run the program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Set background
    background = pygame.image.load("background.jpg")
    display.blit(background, (0, 0))

    # Get the pet details
    pet_details = ui.pet_detail()

    # Split the pet_details string into lines
    lines = pet_details.split("\n")

    # Calculate positions
    x = 20  # Left margin
    y = 20  # Top margin
    line_spacing = 10  # Spacing between lines

    # Render and display each line of the pet details
    for line in lines:
        output = output_font.render(line, True, (250, 250, 250))
        display.blit(output, (x, y))
        y += output.get_height() + line_spacing

    # Update display
    pygame.display.update()