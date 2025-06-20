import math
a, b = 5, 10
a, b = b, a
print("Swapped:", a, b)
x, y, z = 1, 2, 3
x, y, z = z, x, y
print("Circulated:", x, y, z)
x1, y1, x2, y2 = 2, 3, 7, 8
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", round(dist, 2))
