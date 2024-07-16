# Question: Write a Python class named Person with a method myfunc that prints "Hello my name is <name>". Create an object of the class and call the method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()