# Unlike list tuple dosent have methods like append(), remove(), pop(), insert(), because tuple is immutable data type
#only methods in tuple are index() and count()

a = (1, 2, 1, 3, 4, 2, 3, 4, 5)
result = a.index(2)
print(result) #1
result = a.index(2, 2 ,7)
print(result) #5

result = a.count(1) #2
result = a.count(2) #2
#########