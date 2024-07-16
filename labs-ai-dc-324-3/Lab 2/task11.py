# Question: Write a Python function named my_function that takes a parameter country with a default value of "Norway" and prints "I am from <country>". Call the function with and without the parameter.

def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")