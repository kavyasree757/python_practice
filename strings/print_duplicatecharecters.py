s = "programming"

duplicates = []

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j] and s[i] not in duplicates:
            duplicates.append(s[i])

result = ""

for ch in duplicates:
    result = result + ch

print("Duplicate characters are:", result)
