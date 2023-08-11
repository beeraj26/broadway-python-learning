#Condition in python or in any programming language is used to make decisions
#we can make conditions in python in three diffrent ways 

#1. simple if 
#2. if....else block
#3. if...elif ladder 

#Note : Nested if conditions are also possible

#1. Simple if 
age = 25
if age > 19:
    print("The person is not a teenager")

#"if condition" always takes truthy or falsy. If the statement is truthy the block inside if condition is executed. If falsy the block inside if is not executed

if age:
    print(f"The person's age is {age}")

vowels = []
if vowels:
    print(vowels)

a = 2 
if a:
    print(f"The number is {a}") #"The number is 2"

#2. If else
age = 18
if age > 19:
    print("The person is not a teenager")
else:
    print("The person is a teenager")

if age:
    print(f"The person's age is {age}")
else :
    print("The age is not provided")

vowels = []
if vowels:
    print(vowels)
else:
    print("The list is empty")  









    