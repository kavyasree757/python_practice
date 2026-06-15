#Exception Handling in Python

#Exception handling is used to handle runtime errors without stopping the program.

#It prevents program crashes and allows smooth execution.
try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Hello")
