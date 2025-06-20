
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    return (x * y) // find_gcd(x, y)
gcd = find_gcd(a, b)
lcm = find_lcm(a, b)

print("GCD of", a, "and", b, "is:", gcd)

print("LCM of", a, "and", b, "is:", lcm)
