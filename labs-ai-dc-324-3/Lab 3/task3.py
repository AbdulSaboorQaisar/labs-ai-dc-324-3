# Write a Python program to guess a number between 1 to 9.

import random

def guess_number():
 number = random.randint(1 , 9)
 guess = None

 while guess != number:
   guess = int(input("Guess a number between 1 to 9: "))
   
   if(guess != number ):
    print("Try again.")
 print("Well Guessed!")

guess_number()