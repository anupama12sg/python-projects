import random

choices = ('r', 'p', 's')

# Dictionary
# key -> value
# 'r' -> '🪨'
# 'p' -> '📄'
# 's' -> '✂️'
emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
user_choice = input("Rock, paper, scissor (r/p/s):").lower()
if user_choice not in choices:
    print("Invalid Choice.")
computer_choice = random.choice(choices)
print(f"Your choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")


# Ask the user to make a choice
# If choice is not valid
#   Print an error message
# Let the computer make a random choice
# Print choices (emojis)
# Detemine the winner
# Ask the user if they want to continue
# If not
#  Exit the game