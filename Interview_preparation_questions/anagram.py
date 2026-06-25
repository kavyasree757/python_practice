s1 = "listen"
s2 = "silent"

if len(s1) == len(s2) and sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")
