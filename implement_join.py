a = ['python', 'linux', 'pytest']

result = ""

for i in range(len(a)):

    result = result + a[i]

    if i != len(a)-1:

        result = result + " "

print(result)
