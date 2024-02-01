import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Instantiate a Circle object with a radius of 5
circle_instance = Circle(10)

# Calculate and display the circumference and area
circumference = circle_instance.calculate_circumference()
area = circle_instance.calculate_area()

print(f"Circle with radius {circle_instance.radius}:")
print(f"Circumference: {circumference}")
print(f"Area: {area}")
