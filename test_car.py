#This Python file will serve as the testing/main program that needs to be run.
#Wherein the accelerate method and brake method should be called five times each, and speed should be displayed each time.

#Import class
from car_class import Car
from progs_design import ProgramDesign 
from colorama import Back, Fore, Style 

#Initialize class variable
design = ProgramDesign()

#Program Introduction
design.car_header()
design.greetings()
#Program brief instruction
print("This program will use accelerate 5 times and brake 5 times, then showing the speed each time.\n")
design.loading_bar()

#Create car object
test_car = Car(2020,"BMW")

#Call the accelerate method (5 times)
for i in range (5):
    test_car.accelerate()
    #Get speed (each time)
    speed = test_car.get_speed()
    #Display speed (each time)
    print(f"{Fore.LIGHTGREEN_EX}\nAccelerating...(+ 5 speed)\n")
    print(f"{Fore.LIGHTYELLOW_EX}Current Speed: " + str(speed))
    print(speed*"▄▄")
#Call the brake method (5 times)
for i in range (5):
    test_car.brake()
    #Get speed (each time)
    speed = test_car.get_speed()   
    #Display speed (each time)
    print(f"{Fore.LIGHTGREEN_EX}\nBrake...(- 5 speed)\n")
    print(f"{Fore.LIGHTYELLOW_EX}Current Speed: " + str(speed))
    print(speed*"▄▄") 

#Program footer
design.program_footer()