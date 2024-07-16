# Question: Write a Python program that prints all letters except 'e' and 's' in the string 'geeksforgeeks'.

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)