#list=[9,8,7,6,5,4,3,2,1]
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(map(int, input().split()))
start = 0
end = len(a) - 1

while start < end:
    a[start], a[end] = a[end], a[start]

    start += 1
    end -= 1

print(a)
