count = 0

with open("sample.txt", "r") as file:
    for line in file:
        words = line.split()
        count += len(words)

print("Number of words:", count)    
