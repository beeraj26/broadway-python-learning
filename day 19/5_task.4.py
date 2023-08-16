"""
WAP to delete all the occurences of a specific characher in a given string
- S = "All the occurences of a specified character in a given string"
input = "a"
Output = "ll occurences of specifirs chrcter in string in given string"
"""
S = "All the occurences of a specified character in a given string"
char = input("Pick a character")
result = ""
for each in S:
    if each.lower() == char.lower():
        continue
    result += each
print(result)



