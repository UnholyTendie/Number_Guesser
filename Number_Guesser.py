# Ashton Wood
# 03-29-2023
# Number Guesser
# If and else statements to check values

import random

# initialize variables
secret = random.randint(1,10)
try:
    guess = int(input("Enter a number between 1 and 10: "))


# Testing if guess equals number
    if guess < secret:
        print("too low, the number was", secret)
    elif guess > secret:
        print("too highthe number was", secret)
    else: 
        print("You got it")
# Input Validation
except ValueError:
    print ("Please enter a number next time")