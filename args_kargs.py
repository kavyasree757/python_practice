def employee(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

employee(name="Sandeep", age=25, city="Hyderabad")
