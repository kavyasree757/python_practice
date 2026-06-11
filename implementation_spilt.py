s = "python linux pytest"

word = ""
result = []

for i in s:

    if i != " ":

        word = word + i

    else:

        result.append(word)

        word = ""

result.append(word)

print(result)
