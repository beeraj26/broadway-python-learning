n = int(input("Enter a number"))
summ = 0 
for i in range(1, n+1):
    if n % i == 0:
        summ += 1

if summ == 2:
    print(f"{n} is prime")
else:
     print(f"{n} is composite")