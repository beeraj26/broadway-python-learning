#TASK 2

#write a program to find the frequency of the input number in a list [5,2,3,5,3,2,3,3,1,4]
a = [5,2,3,5,3,2,3,3,1,4]
number = int(input("pick a number"))
count = a.count(number)
print(f"count of the number {number} in the list is", count)
