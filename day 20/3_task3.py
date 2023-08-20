#Create a clas person with instance attributes name and age. create a method get detail in this class to print name and age


class Person:
    name = "Leo"

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def description(self): 
        return f"Person name is {self.name} and His age is {self.age}"
 

p1 = Person("Leo", "19") 
print(p1.description())


