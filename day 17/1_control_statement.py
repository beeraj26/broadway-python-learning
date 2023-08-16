#break, continue and pass are the control statement in python. they can alter the normal flow of the program

#break 
for i in range(10):
    if i == 4:
        break
    print(i) #0, 1, 2, 3

n = 0 
while n <= 10:
    if n == 7:
        break
    print(n) # 0, 1, 2, 3, 4, 5 ,6
    n += 1 

#Continue 

for i in range(10):
    if i == 4:
        continue
    print(i) #0, 1, 2, 3, 5, 6 ,7, 8, 9

n = 0 
while n <= 10:
    n += 1
    if n == 7:
        continue
    print(n) # 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11

#pass 
#pass is used to pas the block of code. it literally does nothing. It is also used n the place where code may occur in future 
def addition(a, b):
    pass
    




