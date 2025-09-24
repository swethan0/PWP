import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


# Example usage
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")
