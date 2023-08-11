# Strings are immutable and sequence data- types in python. 
# Creatin an empty string. 

a = "" # Empty string 
b = '' # empty string
c = """""" # empty string
d = str() # empty string

#Creating a non empty string 
a = "hello world" 
b = 'Python is a high level language'
c = """
Hello World. 
Python is awesome. 
"""


# Quote characters
a = "i'm learning python"
b = 'He said, "Python is easy to learn"'

#We can also use escape characters for in strings with quote
a = 'i\'m learning Python'
b = "he said, \"python is easy to learn \""

# Escape character are the characters in python which supress the actual python meaning and gives new meaning to that characters.
#\', \", \n, \t, etc are examples of escape characters.

print("Hello\nWorld") #Print Hello in fisrt line and World in second line 
print("Hello\tWorld") #Print Hello, a tab, World. 


#Python also has Triple quotes strings 
message = """
I'm learning python 
"""
message = '''
I'm learning python 
'''

# Theres is no need for \' (escape sequence) for triple quoted strings. 
#Triple quoted strings are not only used as normal strings, but are also used to add code description in function, classes and as multiline 

def addition(a, b):
    """


    :param a: any integer value 
    :param b: any integer value 
    :return: sum of a and b 
    """
    return a + b 

help(addition)

