"""
number guessing game

Task: Below are the steps:

Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses.

"""

import random
import math

#take the range

lower_range = int(input("Enter the starting value: "))
upper_range = int(input("Enter the ending value: "))

#generating the random  number
random_number = random.randint(lower_range,upper_range)

print("You've only ",round(math.log(upper_range - lower_range + 1, 2))," chances to guess the integer!")
 

#counter to track the number of chances taken by the player to guess the number right

user_guess_count = 0

while user_guess_count < math.log(upper_range-lower_range+1,2):
    user_guess_count += 1

    #guess number input
    guess = int(input("Guess a number: "))

    #conditions 
    if guess == random_number:
        print("Congratulations you did it in ",user_guess_count," try")
        break
    elif guess < random_number:
        print("You guesses too low!")
    else:
        print("You guessed to high!")

if user_guess_count >= math.log(upper_range-lower_range+1,2):
    print("The number is %d",random_number)
    print("Better luck next time!")


