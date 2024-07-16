# Write a Python program that prints each item and its corresponding type from the following list. 

# Sample list
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

# Iterate through each item and print its type
for item in datalist:
 print(f"Item: {item} - Type: {type(item)}")