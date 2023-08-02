# Remove() Method
# Remove method takes list item as a parameter.

vowels = ['a', 'e', 'i', 'o', 'u']
vowels.remove('e')
print(vowels)

#if we pass a parameter not present in  the list then it raises error

vowels.remove('p') #It raises ValueError

#Pop Method
# Pop takes index as a parameter 
vowels = ['a', 'e', 'i', 'o', 'u']
vowels.pop(2)
print(vowels)

# Pop() method also returns a value from the index passed as a parameter
# In the above example resut gives 'i' because 'i' is at 2nd index. And, finally 'i' also removed from the list vowels

#clear() method. It clears the list 

vowels = ['a', 'e', 'i', 'o', 'u']
vowels.clear() # It clears just the list 
print(vowels) #[]

# Index() Method. It takes list item as an argument.
vowels = ['a', 'e', 'i', 'o', 'u']
vowels.index("o")
print(result) #3

# Index method also takes starts and end as parameters.

vowels = [5, 4, 10, "o", "u", 10, 4]
result = vowels.index(4, 2, 8)
print(result) # =6

vowels = [5, 4, 10, "o", "u", 10, 4]
result = vowels.index(2, 4, 8)
print(result) # error

# Count() method takes list item as a parameter and returns the number of repetition of that item
vowels = ['a', 'e', 'i', 'o', 'u' 'o', 'o', 'a', 'i']
print(result) #2
print(vowels.count)


