lines = 0
words = 0
characters = 0

with open("sample.txt", "r") as file:
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

print("Lines:", lines)
print("Words:", words)
print("Characters:", characters)
