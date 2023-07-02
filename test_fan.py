#Write a test program

#Import fan class
from fan_class import Fan
from fan_ui import UserInterface
from progs_design import ProgramDesign 

#Initializing class
ui = UserInterface()
design = ProgramDesign()

#Program header
design.fan_header()
design.loading_bar()

#Create two fan objects
#Object 1
ui.obj1_display()
#Object 2
ui.obj2_display()

#Program footer
design.program_footer()