k=input("Enter a string:\n")
rev=""
for char in k:
    rev=char+rev
if (k==rev):
    print("Given string is palindrome")
else:
    print("Given string is not a palindrome")
