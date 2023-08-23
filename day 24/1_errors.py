#In python the errors can be broadly classified into two sections:
#1. Syntactic Error
#2. Non- Syntactic Error 

#Syntactic Error 
#=> This type of error offurs when you mess up with grammer of the language 
#For example: making typo in keywords, messing up with indentations, whitespaces at unwanted places

 # a = 1 #Syntax error because of white space 
#fo i in range(10): (Syntax error because of the type in keyword)
pass
"""
 if a:
print("Hello") #Indentation Error
"""

#2 Non syntactic Errors 
#=> These are all the errors except syntax error. They can further be classified in followings:
#1. Typeerror
#2. Valueerror
#3. ZeroDivisionError
#4. AttributeError
#5. KeyError
#6. IndexError
#7. NameError
#8. ModuleNotFoundError

#TypeError 
# It is raised when operations in diffrent datatypes are performed which is not acceptable
#For example: 2 + "Hello". Int and String can't be operated with '+' operator 2+ "Hello" raises error

#ValueError
#It is raised if we try to convert a datatype to other datatype which is not possible 
#For eg int("Hello"). This raises Error.

#ZeroDivisionError 
#it is raised when we try to divide an object with 0 
#print(3 / 0) #ZeroDivisionError

#Attribute Error
#It is raised if an object tries to get an attribute which is not present in that object
#For Example: If a list object tries to access the join() method. join() is actually a method in string.
# a = [1, 2, 3]
# a.joint(" ") #Attribute Error

#KeyError
#std = {"name": "John", "address": "KTM"}
#print(std["phone"]) #KeyError 

#IndexError 
data = [1, 2, 3, 4]
print(data[10]) #Index Error

#Name Error
#a = 1 
#print(b) #Name Error: 'b' is not defined

#ModuleNotFoundError

#import mat #ModuleNotFoundError because "mat" is not a valid package

