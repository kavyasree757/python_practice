class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car brand is", self.brand)


c1 = Car("Ford")

c1.show()
