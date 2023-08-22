#Create a class Circle with an attribute radius. Create two objects of circle c1 and c2. Add the radius of the circles and print the result.Do the above task using a method and then a magic method.Compare the size of the circle and print the result using magic method.



class Cricle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, obj2):


c1 = Circle(3)
c2 = Circle(5)
result = c1.raduis + c2.raduis
print(result)
