num = int(input("Enter a number: "))
original = str(num)
reversed_num = original[::-1]

if original == reversed_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
