# Question: Write a Python class named Person with an __init__ method that assigns name and age. Create an object of the class and print the properties.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)