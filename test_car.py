#Next, design a program that creates a Car object then calls the accelerate method five times.
#After each call to the accelerate method ,get the current speed of the car and display it. 
#Then call the brake method five times. 
#After each call to the brake method, get the current speed of the car and display it.

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
    print(speed)
#Call the brake method (5 times)
for i in range (5):
    test_car.brake()
    #Get speed (each time)
    speed = test_car.get_speed()    
    #Display speed (each time)
    print(speed)