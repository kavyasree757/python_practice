a=[10,20,30,40,50]
large=second=a[0]
for i in a:
    if i>large:
        second=large
        large=i
    elif i>second and i!=large:
        second=i
print(second)
