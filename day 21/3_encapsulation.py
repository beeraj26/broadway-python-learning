#Encapsulation is the proces of the data hiding in OOP approach od programming.
#Using this feature we make our attribute private, public or/ and protected.

#Public Attributes 
#These attributes are accesible from both inside the class and outside the class

class Vehicle:
    engine_type = "Petrol"

    def description(self):
        return f"The vechile has{self.engine_type}engine"
    
v = Vehicle()
print(v.engine_type) #Petrol

#Protected 
#These attributes should accesible from the same class or the child class only.

class Vehicle:
    _color = "Blue"    #private member because of single underscore in the begining of the variable


    def color_desc(self):
        return f"The color of the vehicle is {self._color}"
    
class Bike(Vehicle):
    def color_desc(self):
        print(f"The color of the bike is {self._color}")

b = Bike()
print(b._color) #Blue 
# Python is flexible so it also allows the protected members to be accessible from outside the class but it is notrecomended to do so 


#Private Attributes 

class Vehicle:
    __color = "red" #private member because of double underscore in the begining of the variable
    def color_desc(self):
        return f"the color of the cehicle is {self.__color}"

v = Vehicle()
print(v.__color) #AttributeError
print(v.color_desc()) 
