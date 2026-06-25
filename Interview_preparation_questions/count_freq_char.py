k=input("Enter a string:")
d={}
for i in k:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
