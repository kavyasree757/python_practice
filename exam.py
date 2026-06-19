filename=input("Enter file name:")
keyword=input("Enter the keyword you wanted to find:")
with open(filename,"r") as file:
    content=file.read()
if keyword in content:
    print("keyword found in file")
else:
    print("keyword is not found in the file")

