#Function / Method Overloading
#If the function is defined inside the class then the function is called a method. Method are called using object 
#Function overloading is a term used in the programming if the same function defination is repeated multiple times.
#Python does not support function overloading or method overloading 


def addition(a, b):
    return a+b

def addition(a, b, c):
    return a + b + c 

r1 = addition(2, 3) #It raises error 
r2 = addition(2, 3, 4) 
print(r1)
print(r2)

#Even we have defined two addition functions with diffrent number of parameters, but the latest one only consider by Python.
#This problem can be solved in trikey way 

def addition(a, b, c = 0, **kwargs):
    return a + b + c + sum(kwargs.values())

r1 = addition(2, 3)
r2 = addition(2, 3, 4)
print(r1) 
print(r2) 


class A:
    def test_fxn(self):
        return "I'm learning python"
    
    def test_fxn(seld):
        return "Hello World"
    
obj = A()
print(obj.test_fxn()) #Hello World






