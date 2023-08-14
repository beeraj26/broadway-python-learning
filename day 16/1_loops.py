# Loops are used to run te certain block of codes repeatedly
#These are used to reduce the mannual effort anf perform the task in automated  way
#There are two types of loops in python; for loop and while loop 

#for loop in diffrent data types
vowels = ("a", "e", "i", "o", "u")

for each in vowels:
    print(vowels)

#looping is similar in tuple list and set 
#Now lets see looping in dictionary type

std = {"name": "John", "age": 25, "address": "KTM"}
print(std.keys())

for key in std.keys():
    print(key)

print(std.values())
for value in std.values():
    print(value)

print(std.item())

for keys, values in std.items():
    print(key)
    print(value)

for keys, values in [(1, 2), (2, 3), (3, 4)]:
    print(key) # 1
    print(value) #3

#range() function:
# We can gice 3 parameters in the range function range(start, end, step_size)

a = range(10) # gives form 0 to 9; 10 is exclusive
print(a) #range object
print(list(a)) #[1, 2, 3, 4, 5, 6 ,7, 8, 9]

a = range(2, 10) # gives form 2 to 9
print(list(a)) #[2, 3, 4, 5, 6 ,7, 8, 9]

a = range(2, 10, 2) 
print(list(a)) # [2, 4, 6, 8]

squared = []
for i in range(1, 13):
    squared.append(i**2)
print(squared) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]


squared = [i ** 2 for i in range(1, 13)] # List comprehension
print(squared)

######### enumerate() ########
#enumerate() function can take 2 parameters, iterable and start_value
vowels = ("a", "e", "i", "o", "u")
print(enumerate(vowels)) #<enumerate object
print(list(enumerate(vowels))) #[(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')]

for index, value in enumerate(vowels):
    print(index) # 0, 1
    print(value) # a, i

for index, value in enumerate(vowels, start = 1):
    print(index) # 1, 2, 3, 4, 5 ,
    print(value) # a, e, i, o, u
    






