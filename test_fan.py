#Write a test program

#Import fan class
from fan_class import Fan
from fan_ui import UserInterface
from progs_design import ProgramDesign 

#Initializing class
ui = UserInterface()
design = ProgramDesign()

#Program introduction
design.fan_header() 
design.greetings() 
ui.prog_instructions() 
design.loading_bar() 

#Create two fan objects
#Object 1
ui.obj1_displays()
#Object 2
ui.obj2_displays()

#Program footer
design.program_footer()