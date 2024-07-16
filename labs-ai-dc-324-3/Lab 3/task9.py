def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=' ')
        a, b = b, a + b

# Generate Fibonacci series up to 50
fibonacci_series(50)



def fizzbuzz():
    for num in range(1, 51):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Print FizzBuzz for numbers from 1 to 50
fizzbuzz()