# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = [1,2,3,4,5,6,7,8,9]

def count_number(numbers):
    even_count = 0
    odd_count = 0
    
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

even_count, odd_count = count_number(numbers)

print(f"Number of even numbers :{even_count}") 
print(f"Number of odd numbers :{odd_count}") 