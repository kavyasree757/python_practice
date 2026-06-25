ords = line.split()
word = input("Enter the word to search: ")

count = 0

with open("sample.txt", "r") as file:
    for line in file:
        words = line.split()

        for w in words:
            if w == word:
                count += 1

print("Occurrence of", word, "is", count)
