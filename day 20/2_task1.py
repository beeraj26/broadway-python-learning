class Occupation:
    category = "car" 

vehicle = Vehicle() 
print(vehicle.category) 

print(Vehicle.category) 

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