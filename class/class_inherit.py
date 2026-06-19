#
'''inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.'''
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(self.name)
class Dog(Animal):
    pass

dl=Dog("Rex")
dl.speak()
