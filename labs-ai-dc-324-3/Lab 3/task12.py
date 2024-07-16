def binary_divisible_by_5(binary_numbers):
    # Split the input string into individual binary numbers
    binary_list = binary_numbers.split(',')
    
    # List to store binary numbers divisible by 5
    divisible_by_5 = []
    
    # Check each binary number
    for binary in binary_list:
        # Convert binary number to decimal
        decimal = int(binary, 2)
        # Check if divisible by 5
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    
    # Join the list into a comma-separated string
    return ','.join(divisible_by_5)

# Input sequence of comma separated 4 digit binary numbers
binary_numbers = input("Enter 4-digit binary numbers separated by commas: ")

# Get the binary numbers divisible by 5
result = binary_divisible_by_5(binary_numbers)

# Print the result
print("Binary numbers divisible by 5 are:", result)