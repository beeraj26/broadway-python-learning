# Set in python in python are mutable. However, every elements of set must be immutable
# Creating an empty set
a = set() #This is proper way of creating an empty set.

a = {} #This is not an empty set rather it is a dictionary.


#Creating non-empty set
a = set([1, 2, 3 ,4])
print(a) # {1, 2, 3, 4}

a = {1, 2, "a", "b", "apple", True}
print(set(1, 2, 2, 1, 3, 3))

#Set only takes unique elements
print(set([1, 2, 2, 1, 3, 3]))



