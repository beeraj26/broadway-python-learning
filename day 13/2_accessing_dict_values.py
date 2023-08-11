vowels = ["a", "e", "i", "o", "u"]
print(vowels[4]) #u

#Accessing dictionary is similar to that of accessing list elements
student = {"name": "Johan", "age": 25, "department": "CS"}
dept = student["department"]
print(dept) #CS

name = student["name"]
print(name) #Johan

print(student["dob"]) #This raises error

#accessing values using get() method 
department = student.get("department")
print(department) #CS
dob = student.get("dob") #This raises Key Error

# accessing values using get() method
department = student.get("department")
print(department)  # CS
dob = student.get("dob")
print(dob)  # None

#Adding key-value pair in a dictionary
vowels = ["a", "e", "i", "o"]
vowels.append("u")
vowels.insert(2, "A")

std = {"name": "Johan", "age": 25, "department": "CS"}
std["dob"] = "10 July"
print(std) #{"name": "Johan", "age": 25, "department": "CS"}

std.update(roll_no = 12)
print(std) #{'name': 'Johan', 'age': 25, 'department': 'CS', 'dob': '10 July', 'roll_no': 12}


std["name"] = "leo"
print(std)

#Removing a Key-value pair from a dictionary 

std = {'name': 'Johan', 'age': 25, 'department': 'CS', 'dob': '10 July', 'roll_no': 12}
result = std.pop("dob")
print(result) # 'dob': '10 July'
print(std) #{'name': 'johan', 'age': 25, 'department': 'CS'}

#result = std.pop ("address") #Key error
#print(result)

result = std.popitem()
print(result) # ('roll_no', 12)

print(std) #{'name': 'Johan', 'age': 25, 'department': 'CS'}

std.clear()
print(std) #{}

del std # del the object



    