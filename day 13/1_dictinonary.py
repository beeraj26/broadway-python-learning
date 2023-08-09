#Dictionary is the mutable datatype in python
#They have the elements in key value pair format.
# It is also the sequential datatype like list and tuple

#Creating an empty dictionary 
a = dict() #Empty dictionary 
a = {} # this is also an empty dictionary 

#Creating a non-empty dictionary
student = {"name": "Johan", "age": 25, "department": "CS"}
print(student) # {'name': 'Johan', 'age': 25, 'department': 'CS'}

student = dict(name ="johan", age = 25, department = "CS")
print(student) #{'name': 'johan', 'age': 25, 'department': 'CS'}

student = dict({"name": "Johan", "age": 25, "department": "CS"})
print(student)

#student = dict([("name": johan)])


#Creating a list of dictionaries 

student =[
    {"name": "Johan", "age": 25, "department": "CS"}
    {"name": "Jane", "age": 36, "department": "IT"}
    {"name": "Hary", "age": 29, "department": "Physics"}
]
print(student)


