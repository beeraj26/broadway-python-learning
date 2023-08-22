# Operator overloading is the way of defining how an operator behaves in its operations 
#For example '+' operator in the integer operatin behaves diffrent from the string operation

a = 1 
b = 2
print(a + b) #3 

m1 = "Hello"
m2 = "World"
print(m1 + m2) #HelloWorld

#Such operators functions are defined in the built-in classes of Python.These methods are called magic methods. __add__(), __mul__(), __sub__(), __gt__()etc, are the example of magic method

a = 1 
b = 2
print(a + b) #3
print(a.__add__(b))  #3