# Mutable and immutable objects ###
'''
If an object once created can be changed later then the object is a mutable object

BUT IF AN OBJECT ONCE CREATED CAN NEVER BE CHANGED THROUGHOUT ITS LIFE CYLCE THEN IT IS AN IMUTABLE OBJECT.

list, dictanory, set are the example of mutable object 
number tuple, boolean, ,string are the example of imutale object
'''

a = ['a''b''c']
a[1] = 'd'
a

b = (1,2,3)
b[1] = 5 #this raises error
