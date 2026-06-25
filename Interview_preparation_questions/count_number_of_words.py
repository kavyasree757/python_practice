s = input("Enter a sentence: ")

count = 1

for ch in s:
    if ch == " ":
        count += 1

print("Number of words:", count)
