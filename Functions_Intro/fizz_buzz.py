"""
    Implement the Fizz Buzz Game Logic Using a Python Function
    Develop the code for this exercise in your IDE.
    This on-line Python interpreter can execute your code,
    and check the results, but it's not an IDE.

    You won't get meaningful error messages, for one thing.

    Once you think your code works, copy and paste the code in here,
    to complete the exercise.

    For this exercise, you'll write a function that returns
    the appropriate response, in the game of fizz buzz.

    It's a simple game, usually played with 2 or more people.

    You start counting, in turn. That's easy enough,
    but there's a complication.

        If the number is divisible by 3, you say "fizz" instead.

        If it's divisible by 5, you say "buzz".

        And if it's divisible by both 3 and 5, you say "fizz buzz".

    The function must be called fizz_buzz

    Your fizz_buzz function should return the correct word ("fizz",
    "buzz" or "fizz buzz"), or the number if it's not divisible
    by either 3 or 5.

    The function will always return a string.
    When you return the number, therefore,
    you should convert it to a string first.

    Remember to annotate your function, and include a Docstring.

    Include a for loop, to test your
    function for values from 1 to 100, inclusive.

    Create a fizz_buzz function that returns "fizz" for multiples of 3,
    "buzz" for multiples of 5,
    "fizz buzz" for multiples of both,
    and the number as a string otherwise.

"""

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


# # Manual Testing
# while True:
#
#     user_input = input("Please enter a number (or 'q' to quit): ")
#
#     if user_input == 'q':
#         break
#
#     try:
#         user_input = int(user_input)
#
#     except ValueError:
#         print("Please input a valid number (e.g., 1)")
#         continue
#
#     print(fizz_buzz(user_input))

# # # automated testing for numbers 1 - 100:
# for i in range(1, 101):
#     print(fizz_buzz(i))

"""
next challenge:
    Replace the loop (above) that will:
        - Loop to play the game.
        - The 'computer' will start with the value 1
            - computer will print out its next value.
        - The 'player' and the 'computer' will take turns.
            - The 'player' will type in their response
        - and so on..
        - The game ends when the player makes a mistake,
            - or gets to 100.
        - if the player gets it wrong, they lose
        
    Write first your code in pseudocode
    
    START
        SET MAX_TURN TO 100
        
            FOR t FROM 1 TO MAX_TURN DO
                
                IF t MOD 2 == 1 THEN
                    DISPLAY "Computer's Turn"
                    SET answer to fizz_buzz(t)
                    DISPLAY answer
                ELSE
                    DISPLAY "Your Turn"
                    PROMPT user for input
                    SET user_input TO entered value
                    
                    SET correct_answer TO fizz_buzz(t)
                    
                    IF user_input NOT EQUAL to correct_answer THEN
                        DISPLAY "Incorrect! You Lose."
                        EXIT LOOP
                    END IF
                
                END IF
            
            ELSE
                DISPLAY "Congratulations! You reached " + MAX_TURN + "!"
            END FOR
        
    END
"""

MAX_TURN = 10

print("Fizz Buzz Game — Player vs Computer")
print("Type the correct response. Game ends if you get it wrong.\n")

for t in range(1, MAX_TURN + 1):
    print(f"\nTurn {t}")
    if t % 2 == 1:
        computer_answer = fizz_buzz(t)
        print(f"Computer says: {computer_answer}")
    else:
        # Ask user for input
        user_input = input("Your turn: ").strip().casefold()

        # Set correct_answer
        correct_answer = fizz_buzz(t)

        # check if user_input is not correct
        if user_input != correct_answer:
            print(f"Wrong! the correct answer was: {correct_answer}")
            print("Game Over. you lose.")
            break

else:
    print(f"Congratulations! You reached {MAX_TURN} and won the game!")
