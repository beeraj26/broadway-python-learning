# Copy()
std1= {"name": "John", "age": 25}
std2 = std1.copy() #{"name": "John", "age": 25}
print(std2) #{"name": "John", "age": 25}
print(std1) #{"name": "John", "age": 25}




#get()
student = {"name": "John", "age": 25}
name = student.get("name")
print(name) 

roll = student.get("roll")
print(roll) #roll
roll = student.get("roll", 89)
print(roll) #89

name = student.get("Name", "Ram")
print(name) #John

#Items()
std1= {"name": "John", "age": 25, "roll": 26}
print(std1.items()) #dict_items([('name', 'John'), ('age', 25), ('roll', 26)])

#keys()
std1= {"name": "John", "age": 25, "roll": 26}
print(std1.keys()) #dict_keys(['name', 'age', 'roll'])

#values()
std1= {"name": "John", "age": 25, "roll": 26}
print(std1.values()) #dict_values(['John', 25, 26])

#pop()
std1= {"name": "John", "age": 25, "roll": 26}
std1.pop("age") #25
print(std1) #{'name': 'John', 'roll': 26}

#popitem()
std1= {"name": "John", "age": 25, "roll": 26}
result = student.popitem() 
print(result) #roll 26
print(student) #"name": "John", "age": 25

#update()
std1= {"name": "John", "age": 25, "roll": 26}
std1.update(address="KTM")
print(std1) #{'name': 'John', 'age': 25, 'roll': 26, 'address': 'KTM'}

#fromkeys()
a = dict()
a.fromkeys([1, 2], "a")
print(a) #{1: 'a', 2: 'a'}
print(result) #{1: 'a', 2: 'a'}

#setdefult()
std1= {"name": "John", "age": 25, "roll": 26}
std1.setdefault("name", "leo")
print(std1) #nothing will change.

std1= {"name": "John", "age": 25, "roll": 26}
std1.setdefault("address", "bkt")
print(std1) #{'name': 'John', 'age': 25, 'roll': 26, 'address': 'bkt'}









