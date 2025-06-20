text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
char_to_count = input("Enter a character to count: ")
count = text.count(char_to_count)
print(f"'{char_to_count}' occurs {count} time(s) in the string.")

old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
replaced_text = text.replace(old_char, new_char)
print("Updated string:", replaced_text)
