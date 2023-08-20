#Inheritance is the transfer of properties and methods to the child class from the parent class
#Types of inheritance in python 
#1. Single Inheritance
#2. Multiple Inheritance
#3. Multilevel Inheritance
#4. Hiearchical Inheritance
#5. Hybird Inheritance

class Vehicle: #parent class
    engine_type = "petrol_engine"

class Bike(Vehicle):
    wheels = "two"

class Car(Vehicle): 
    wheels = "four"

car = Car()
print(car.engine_type) #petrol type
print(car.wheels) #"four"

class Cycle(Bike):
    engine_type = "None"

#Single Inheritance

class A:
    pass

class B(A):
    pass


#Multiple Inheritance

class A:
    pass

class B:
    pass

class C(A , B):
    pass

#Multilevel Inheritance

class A:
    pass

class B(A):
    pass

class C(B):
    pass

#Hierarchical Inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

#mro => mrp stands for method resolution order, it is the order in which atributes in inheritance is searched 


#Hybird Inheritance 

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E:
    pass

e = E()
print(E.mro())







