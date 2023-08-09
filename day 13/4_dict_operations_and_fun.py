#Membership Operation
#Membership is checked only in dictionary keys but not in values. 
std = {'name': 'Johan', 'age': 25, 'department': 'CS'}
print("name" in std) # true 
print("Johan" in std) # false 


# Built-In functions 
print(len(std)) #3


result = sorted(std)
print(result) #['age', 'department', 'name']

print(str(std)) #"{'name': 'Johan', 'age': 25, 'department': 'CS'}"



