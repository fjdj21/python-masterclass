# imports here:

# variables here:
low = 1
high = 1000
guesses = 1

print(f"Please think of a number between {low} and {high} values.")
input("Press ENTER to start")

while low != high:
    print(f"\tGuessing in the range of {low} to {high}.")
    guess = low + (high - low) // 2  # calculates the mid point between the high and low values
    high_low = input(f"My guess is {guess}. Should I guess higher or lower? "
                     f"Enter h or l, or c if my guess was correct: ").casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
        # pass # placeholder to be syntactically correct
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less then the guess.
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses!")
        break
    else:
        print(f"Please enter 'h', 'l', or 'c'")
        continue

    #guesses = guesses + 1
    guesses += 1
else: #else for while loop
    print(f"You thought of the number: {low}")
    print(f"I got it in {guesses} guesses.")
