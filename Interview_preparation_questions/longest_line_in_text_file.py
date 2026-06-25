with open("sample.txt", "r") as file:
    longest = ""
    for line in file:
        if len(line) > len(longest):
            longest = line

print("Longest line is:")
print(longest)
print("Length:", len(longest))
