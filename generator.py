def demo():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")
    yield 30

g = demo()

print(next(g))
print(next(g))
print(next(g))
