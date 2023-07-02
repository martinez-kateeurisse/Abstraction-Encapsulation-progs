#This python file will serve as the main file that will be run.

#write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. 
#This data should be stored as the object’s attributes. 
#Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.

from pet_class import Pet

#Store the data as object attributes
pet = Pet(" "," "," ")

#Create an object of the classs
# Ask user to enter the name
name = input("Please enter the pet's name: ")
#Set the name based on user's input
pet.set_name(name)

# Ask user to enter the type
animal_type = input("Please enter the pet's animal type: ")
#Set the animal type based on user's input
pet.set_animal_type(animal_type)

# Ask user to enter the age
age = float(input("Please enter pet's age: "))
#Set the nage base on user's input
pet.set_age(age)

#Use methods to retrieve and display output
print("PET DETAILS")
print("Pet's Name: ", pet.get_name())
print("Pet's Animal Type: ", pet.get_animal_type())
print("Pet's Age: ", pet.get_age())