s = input("Enter a string: ")

ch = input("Enter character: ")

count = 0

for char in s:
    if char == ch:
        count += 1

print("Frequency:", count)
