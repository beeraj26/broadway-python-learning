# Tuples are immutable data type in python. They are sequential data type like list, string, dictionary and set. 
# Creating an empty tuple
a = tuple() #tuple() built-in function can be used to create a tuple.
print(a) 
a = ()
print(a)

#Creating non-empty tuples
a = (1, 2, "a", "e", [1, 3]) #Tuples elements are enclosed in paranthesis or small brackets 
print(a)
a = tuple([1, 2, 3]) #Tuple elements are enclosed in parenthesis or small brackets 
print(a)
a = (1 ,2, 3) 

######### Tuple packing and unpacking ###########
a = 1
#print(type(a)) = #here 'a' is int type
# 
# But if we add ','  at the last it is tuple packing 
a = 1, 
print(a) #here "a" is tuple type

a = 1, 2, 3
print(a) #This is also a tuple(1, 2, 3)

a = 1, "a", [1, 2], {1, 2}

#Unpacking 
a, b = 1, 2
print(a) #1; integer type
print(b) #2; integer type

a, b, c = 2, "hello", ["a", "e", "i"]
print(a) #2
print(b) #hello
print(c) # ['a', 'e', 'i']

#If number of elements in LHS is not equal to RHS then it raises error in tuple unpacking 
a, b, c = 1, 2, 3, 4 #too many values to unpack
print(a)
print(b) 
print(c)

a, b, c= 1, 2 #ValueError: not enough values to unpack
print(a)
print(b)
print(c)

a = 2
b = 4 
print(a) 
print(b)

c = a
a = b
b = c






