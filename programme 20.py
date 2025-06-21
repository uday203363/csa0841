
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 10
}


frequency = {}


for value in my_dict.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1


print("Original dictionary:", my_dict)
print("Frequency of values:", frequency)
