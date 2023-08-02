### List Indexing ###
#List indexing starts from 0 for forward indexing and -1 for the backward indexing

vowels = ['a' 'e' 'i' 'o' 'u']
print (vowels [0]) # => 'a'
print (vowels [2]) # => 'i'
#print (vowels [5])# => 'it raises error'

print(vowels[-1]) # => 'u'
print(vowels[-3]) # => 'i'
#print(vowels[-6]) # => 'it raises index error'

vowels[2] = "I" # Assigning item to the list at 2nd position
print(vowels)

vowels[-1] = #Assingning item to the list at last position with negative indexing

vowels = ['a' 'e' 'i' 'o' 'u']

a = ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j']
print(a[:])# = ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j']
print(a[0]) #= ['a' 'b' 'c' 'd' 'e' 'f' 'g]
print(a[:7]) #= ['a' 'b' 'c' 'd' 'e' 'f' 'g']

### list slicing ###

#In sllicing, first index is inclusive but the second index is always exclusive.

print(a[3:]) # =['d' 'e' 'f' 'g' 'h' 'i' 'j']

print(a[2:6]) # ['c' 'd' 'e' 'f']
print(a[6: 2]) # []

print(a[-7: -2]) # ['d' 'e' 'f' 'g']
print(a[-2: -7]) # []
print(a[:-2]) # ['a' 'b' 'c' 'd' 'e' 'f' 'g' 'h']
print(a[2:-2]) # ['c' 'd' 'e' 'f' 'g' 'h']
print(a[-3:]) # ['h' 'i' 'j']

### list operation ###
#In every data-types operations, methods, built-in function, should be studied carefully 
