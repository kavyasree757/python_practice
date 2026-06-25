with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    if f1.read() == f2.read():
        print("Files are identical.")
    else:
        print("Files are different.")
