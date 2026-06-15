a = [10, 20, 4, 45, 99]

largest = second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i

    elif i > second and i != largest:
        second = i

print("Second largest element is:", second)
