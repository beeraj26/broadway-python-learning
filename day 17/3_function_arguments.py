# Arguments in the functions are the elements that are sent in the function call.
# Parameters in the functions are the elements that are present in the function defination

#Types of arguments in a function 
#1. Positional / Required arguments 
#2. Default Arguments 
#3. Arbitrary Arguments 

def addition(a , b, c=5):
    return a + b + c

result = addition(2, 3, 10)
print(result) #15

#Here "a" and "b" are the positional arguments and "c" is a defult argument 
#Positional arguments must be sent during a function call i.e. they are the required arguments
#  # Default arguments are not required in a function call.