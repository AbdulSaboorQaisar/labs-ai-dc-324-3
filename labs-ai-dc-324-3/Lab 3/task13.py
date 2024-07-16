def count_letters_and_digits(input_string):
    # Initialize counters for letters and digits
    letters = 0
    digits = 0
    
    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is a letter
        if char.isalpha():
            letters += 1
        # Check if the character is a digit
        elif char.isdigit():
            digits += 1
    
    return letters, digits

# Input string
input_string = input("Enter a string: ")

# Get the counts of letters and digits
letters_count, digits_count = count_letters_and_digits(input_string)

# Print the results
print(f"Letters: {letters_count}")
print(f"Digits: {digits_count}")