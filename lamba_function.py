#lambda arguments : expression
a = [(1, 3), (2, 1), (4, 2)]

a.sort(key=lambda x: x[1])

print(a)
