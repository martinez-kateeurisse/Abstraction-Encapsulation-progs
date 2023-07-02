#This Python file will serve as the testing/main program that needs to be run.
#Wherein the accelerate method and brake method should be called five times each, and speed should be displayed each time.

#Import class
from car_class import Car

#Create car object
test_car = Car(2020,"BMW")

#Call the accelerate method (5 times)
for i in range (5):
    test_car.accelerate()
    #Get speed (each time)
    speed = test_car.get_speed()
    #Display speed (each time)
    print("Accelerating...(+ 5 speed)")
    print("Current Speed: " + str(speed))
#Call the brake method (5 times)
for i in range (5):
    test_car.brake()
    #Get speed (each time)
    speed = test_car.get_speed()    
    #Display speed (each time)
    print("Brake...(- 5 speed)")
    print("Current Speed: " + str(speed))