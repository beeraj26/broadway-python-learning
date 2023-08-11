#Write a program to prompt for a score between 0.0 and 1.0. If the score is between 0.0 and and 1.0, print a grade using the following table:
#A for >= 0.9
#B for >= 0.8
#C for >= 0.7
#D for >= 0.6
#F for <0.6

percentage = float(input("Enter your percentage"))
if percentage > 1.0 or percentage < 0.0:
    print("Invalid percentage")
elif percentage >= 0.9:
    print("A")
elif percentage >= 0.8:
    print("B")
elif percentage >= 0.7:
    print("C")
elif percentage >= 0.6:
    print("D")
else:
    print("F")
    

