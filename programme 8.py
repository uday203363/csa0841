import math


print("Even Number Series up to 10:")
for i in range(2, 11, 2):
    print(i, end=' ')
print("\n")


print("Fibonacci Series (7 terms):")
a, b = 0, 1
for _ in range(7):
    print(a, end=' ')
    a, b = b, a + b
print("\n")

print("Square Number Series:")
for i in range(1, 11):
    print(i**2, end=' ')

print("Number Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()

print("Pyramid Pattern:")
rows = 5
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '* ' * i)

