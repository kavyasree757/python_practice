s = input("Enter a string: ")

count = 0
vowels = ""

for char in s:
    if char in "aeiouAEIOU":
        count += 1
        vowels += char
if count > 0:
    print(f"The number of vowels in the given string is {count}")
    print(f"The vowels are: {vowels}")
else:
    print("No vowels in the given string")
