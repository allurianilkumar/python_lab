# shapes.py
import math
# Base class for Shape
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
# Subclass for Triangle (Equilateral for simplicity)
class Triangle(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return (math.sqrt(3) / 4) * (self.side ** 2)
    def perimeter(self):
        return 3 * self.side
# Subclass for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
# Demonstrating functionality
shapes = [
    Circle(radius=5),
    Triangle(side=6),
    Square(side=4)
]
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}\n")
