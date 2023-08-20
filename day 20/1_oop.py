#OOP stands for Object Oriented Programming 
#It is the way of the modeling the real world problems into a program
# It has two important componennts;

#Classes are the blue prints of an object 
#Object are the instance of the class 


#Major Features of Object Oriented Programming
#1. Inheritance
#2. Encapsulation
#3. Polymorphism
#4. Abstraction


class Vehicle:
    category = "car" #This is class atribute

vehicle = Vehicle() #This is creating an object of class Vehicle
print(vehicle.category) #This is getting class atribute using an object 

print(Vehicle.category) #This is getting class atribute using a class

vehicle.category = "truck"
print(Vehicle.category) #Car
print(vehicle.category) #Truck

class Vehicle:
    category = "car"

    def __init__(self, doors, color): #This is a constructor
        self.doors = doors #Instance atributte
        self.color = color #Instance atributte

def description(self): #a method inside Vehicle class
    return f"Vehicle is {self.category}. Color is {self.color}.and doors is {self.doors}"

def change_colour(self, color): #This is also a method
    self.color 

v1 = Vehicle(4, "red") 
print(v1.category) #car #get data
print(v1.doors) #4
print(v1.color) #red

v1.category = "bike"
print(Vehicle.category) #"car" #get data
print(v1.category) # "bike" #get data

v2 = Vehicle(2, "Green")
print(v2.doors) #2
print(v2.color) #Green

v2 = Vehicle()

change_colour = "blue"
print(change_colour)


print(description)
#function inside a class is called the method of that class and can be called with the object of than class only







    
