#PYTHON STATEMENT


#back slash can be used to take an statement to the next line
nessage = "hello i'm learning \
    python"

import json, \
csv

#we can use ';' to write multiple statements in a same line
name = "john" ; age = 34

#indentation in python is very important:
# an indentation is equvalent to 4 spaces / 1 tab
# we don't use curly bracecs in python to determine a block of code. instead, we use indentation

#following is an example of a c code

if (a==2) {
    printf("hello world")
        }
# here the block of if condition is determined by indentation 
#for example
a=1
if a ==2:
    print("hello world")
    b == 2:
    print("python")
    print("is")
    print("awesome")
    print("anither message")
print("stg")


#DOCSTRING EXAMPLE 
message = """
python is a high level language.
it is easy to learn
"""
print (message)

message = "i'm learning python"
message = 'he said "hello"'

#escape sequence 
message = 'i\m learning python'