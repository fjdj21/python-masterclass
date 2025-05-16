#imports here
import random

# # helper function
# def print_hint(guess, answer, remaining_attempts):
#     if guess > answer:
#         print(f"Please guess lower, number of attempts left: {remaining_attempts}")
#     else:
#         print(f"Please guess higher, number of attempts left: {remaining_attempts}")

# Declare variables here
highest = 1000
lowest = 1
answer = random.randint(lowest,highest)
quit_code = 0
max_no_of_attempts = 10
attempt = 0
guess = None

# prints here
print(f'answer is {answer}') # TODO: Remove after testing
print(f"Welcome to the Number Guessing Game!")
print(f"Guess a number between {lowest} and {highest}.")
print(f"You have {max_no_of_attempts} attempts left.")
print(f"Type {quit_code} if you want to quit early.")

# logic here
while attempt < max_no_of_attempts:
    try:
        guess = int(input(f"\nAttempt number {attempt + 1}, Enter your guess: "))
        #print(f"attempt try: {attempt}") # TODO : Remove after testing
    except ValueError:
        print("Invalid input, please enter a number")
        continue

    attempt += 1
    #print(f"attempt after increment: {attempt}") # TODO : Remove after testing
    remaining_attempts = max_no_of_attempts - attempt # calculate number of attempts

    if guess == quit_code:
        if attempt == 1:
            print(f"You entered {quit_code}, why'd you leave on your first try having {max_no_of_attempts} attempts.")
            break
        else:
            print(f"Giving up with {remaining_attempts + 1} attempts remaining.")
            break

    if guess == answer:
        if attempt == 1: #First attempt
            print("Wow, you guessed it the first time")
            break
        else: #More than 1 attempt
            print(f"Well done, you guessed it in {attempt} attempts.")
            break
    else: #guess != answer:
        if attempt == max_no_of_attempts:
            print(f"Sorry, you've used all your attempts. The correct answer was {answer}.")
        else:
            if guess > answer:
                print(f"Please guess lower, number of attempts left: {remaining_attempts}")
            else:
                print(f"Please guess higher, number of attempts left: {remaining_attempts}")
