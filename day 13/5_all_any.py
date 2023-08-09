# all(iterable) built-in function
#all() function takes an iterable as a parameter 
#if all the elements of that iterable are truthy then it returns true

result = all([1,2,"john"])
print(result) #True

result = all([0,"jane"])
print(result) #False 


# any(iterable) built-in function
#any() function takes an iterable as a parameter 
#if any the elements of that iterable is truthy then it returns true
print(any(["", {}, 1])) # true
print(any([0, []])) # true

#There is one exeption in all()
result = all([])
#print(result) = #true 

