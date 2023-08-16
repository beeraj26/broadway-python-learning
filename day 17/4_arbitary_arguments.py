# *args and **kwargs are the arbitraty arguments 
#These arguments can take dynamic number of parameters
#They are like an expandable bucket

def addition(*args):
    #print(args) (1, 2, 3, 4)
    #print(type(args)) #Tuples
    return sum(args)

result = addition(1, 2, 3, 4)
print(result)

def addition(**kwargs):
    print(kwargs) #{"a": 1, "b": 2, "c": 3}
    print(type(kwargs)) #dict
    total = sum(kwargs.values())
    print("Sum", total)
    
addition(a= 1, b=2, c= 3)



