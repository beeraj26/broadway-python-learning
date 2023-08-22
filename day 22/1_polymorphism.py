#Polymorphisim means many dors of same the same function or object.
# We can take the example of len, sum, min, max, etc. built in functions to ovserve polymorphism in python

#len() is a built-in function in python which can take any type of iterable as a parameter and gives te length of the iterable

print(len([1, 2, 3])) #3 (list)
print(len((1, 2, 3))) #3 (tupple)
print(len({"name": "Jane", "address": "KTM"})) #2  dict 

#regardless og the datatype, len returns the length of an iterable

#we can classify polymorphism to three diffrent variations in Python 
#1. Function / Method Overloading
#2. Method Overriding
#3. Operator Overloading 


