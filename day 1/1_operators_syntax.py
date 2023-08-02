#operatios are the special symbols in any programming language to carry out Arthematic and Logical Operations

a=1
b=2
c= a+b
#here '='is an asignment operator and'+' is an 
# Arithemetic Operators
#Addition (+)
#Subtraction (-)
#multiplication (*)
#division (/)
#floor division (//) => Floor division removees the deecimal value and only provides the integer towards floor.
 
print(3//2) #it gives 1
print(-3//2) #it gives -2

#exponential (**)
print (3**2) #it gives 9

#modules (%) => gives remainder of a division
print(3 % 2) #it gives 1
print(4 % 2) #it gives 0

#### comprasion / relation operators ####
# ==, <, >, !=, >=, <=, are the relational operatios
print (4== 5) #false



#logical operatiors
#and, or, not are the logical operations and thieir operators are "and", "or" 
#and"not" respectively, the results in logical operations are either True or False

#identical operatios
#identity operators checkc whether the two objects are same or not. 'is' and 'is not' are used for the identity check.

a=1
b=1
print(a is b ) #true
print (id(a))
print (id(b)) #for the same object, id() gives value 


#membership operators
#it is used to check membership of an object in a sequence
print(2 in(1, 2, 3) #true
print(3 not in(1, 2, 3) #false
      
#assignment operator
#the result of any operation can be assigned to a variable using an assignment operator. 
#operator. "=" is a basic asignment operator
#name = "jhon" #here = is an assignment operator

# +=, -=, *=, /=, are also assignment operators
#a=1
#a= a+1 #this line also be written as a += 1
print(a) #2
#a += 1 #3
print(a)


#precedence and associativy 
#precedence of the operators is the ruule that determines which operator should be executes first
# if multiple operators in an operation have the same precedence then the associativity determines the operation sequence.
#normally associavity is form left-right except for the case of '**'

print(2**3**2) #512

#syntax

