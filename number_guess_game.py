# Generate a random number (system does this)
import random

number_to_guess = random.randint(1, 100)

#Loop
guess = int(input("Guess the number between 1 to 100: "))
print(guess)
 # Ask the user to guess the number
 # If the number is not valid
 #  Print an error
 # If the number < guess_number
 #  Print too low
 # If the number > guess number
 #  Print too high
 # Else
 #  Print Congrats! You got that right!
