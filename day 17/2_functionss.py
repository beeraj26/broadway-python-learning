#Functions are the block of codes that are re- usable
#If the same lines of code is repeated at multiple places in the code, then we can define a function for theat code block ad call whereever necessary 

#There are things we need to keep in mind while creating a function:
#1. Function Definition
#2. Function Call 

#lets check a simple function to check whether a number is odd or even 

def is_even(number): #This is a function defination
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_even_n(number):
    return number % 2 == 0


result = is_even(43) #Function call
print(result) #False

def addition(n1,n2): #Function Defination
    return n1 + n2

result = addition(4, 5) #function call
print(result) #9