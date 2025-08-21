class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)
newCircle = Circle(5)

print(newCircle.area())  # Output: 78.53975