filename = input("Enter file name: ")
keyword = input("Enter keyword to search: ")

with open(filename, "r") as file:
    content = file.read()

if keyword in content:
    print("Keyword found")
else:
    print("Keyword not found")
