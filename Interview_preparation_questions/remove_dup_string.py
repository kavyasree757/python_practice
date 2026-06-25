k=input("Enter a string:")
d={}
result=""
for i in k:
    if i not in d:
        d[i]=1
        result=result+i
print(result)        
