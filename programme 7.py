import math

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to find largest number in a list
def find_largest(lst):
    return max(lst)

# Function to calculate area
def area(shape, a, b=0):
    if shape == "circle":
        return math.pi * a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "triangle":
        return 0.5 * a * b
    else:
        return 0
        # Using the functions

# Factorial
print("Factorial of 6:", factorial(6))

# Largest number
numbers = [12, 45, 3, 78, 2]
print("Largest number:", find_largest(numbers))

# Areas
print("Area of circle (radius 5):", area("circle", 5))
print("Area of rectangle (5x10):", area("rectangle", 5, 10))
print("Area of triangle (base=4, height=6):", area("triangle", 4, 6))

