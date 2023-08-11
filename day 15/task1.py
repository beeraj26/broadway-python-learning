#Write a program to input a number and check whether the number is odd or even. 
# Get input from the user
a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")
