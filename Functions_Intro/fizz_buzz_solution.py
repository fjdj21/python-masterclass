def fizz_buzz(n: int) -> str:
    """
        Returns:
            'fizz' if `n` is divisible by 3,
            'buzz' if divisible by 5,
            'fizz buzz' if divisible by both,
            else the number as a string.
    """
    if n % 3 == 0 and n % 5 == 0:
        # print(f"{n} is multiples of 3 and 5")
        return "fizz buzz"
    elif n % 3 == 0:
        # print(f"{n} is multiples of 3")
        return "fizz"
    elif n % 5 == 0:
        # print(f"{n} is multiples of 5")
        return "buzz"
    else:
        return str(n)

input("Play Fizz Buzz. Press ENTER to start")

MAX_TURN = 100

next_number = 0
while next_number < MAX_TURN - 1:

    # Display computer answer
    next_number += 1
    print(f"\nTurn {next_number}") # Display turn number
    print(f"Computer says: {fizz_buzz(next_number)}")

    # add another counter for player's turn
    next_number += 1
    # Assign the correct answer to a variable
    correct_answer = fizz_buzz(next_number)

    # ask for user input:
    player_answer = input("Your turn: ")

    # check if player answer is correct
    if player_answer != correct_answer:
        print(f"You Lose, the correct answer was {correct_answer}")
        break

else:
    print(f"Well done, you reached {MAX_TURN}")
