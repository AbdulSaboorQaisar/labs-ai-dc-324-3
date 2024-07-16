# Write a Python program that prints all the numbers from Oto 6 except 3 and 6.
# Note : Use 'continue' statement.

# Loop through numbers from 0 to 6
for number in range(7):
    # Skip the iteration if the number is 3 or 6
    if number == 3 or number == 6:
        continue
    # Print the number
    print(number, end=' ')