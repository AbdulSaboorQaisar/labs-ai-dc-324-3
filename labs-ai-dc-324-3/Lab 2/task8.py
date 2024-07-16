# Question: Write a Python program that breaks the loop as soon as it encounters 'e' or 's' in the string 'geeksforgeeks'.

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print('Current Letter :', letter)