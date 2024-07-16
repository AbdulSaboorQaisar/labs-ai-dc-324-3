# Write a Python program that accepts a word from the user and reverse it.

def reverse_word(word):
    return word[::-1]

# Accept input from the user
word = input("Enter a word: ")

# Reverse the word
reversed_word = reverse_word(word)
# reversed_word = word[::-1]

# Print the reversed word
print(f"Reversed word: {reversed_word}")