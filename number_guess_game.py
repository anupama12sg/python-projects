# Generate a random number (system does this)
import random

number_to_guess = random.randint(1, 100)

#Loop
try:
    guess = int(input("Guess the number between 1 to 100: "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congrats! You got the right number!")
except ValueError:
    print("Please enter a valid number.")
    

    
# Ask the user to guess the number
 # If the number is not valid
 #  Print an error
 # If the number < guess_number
 #  Print too low
 # If the number > guess number
 #  Print too high
 # Else
 #  Print Congrats! You got that right!
