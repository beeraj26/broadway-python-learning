# Sort() method is used to sort the elements of the list in ascending or desending order and alphabetically for strings

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers = [(5, 4), (3, 2), (1, 9), (6,1)]
# Expected result [(6, 1), (3, 2), (5, 4), (1, 9)]
def sort_with_second_item(data):
    return data[1]

numbers.sort(key=sort_with_second_item)
print(numbers)

numbers[(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]
# Expected result [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]

def sort_with_last_item(data):
    return data[-1]

numbers.sort(key=sort_with_last_item)
print(numbers)

# Reverse() method. It reverse the item of the list 
fruits = ["banana", "apple", "mango"]
fruits.reverse()
print(fruits)

