from ai import call_gpt

def main():
    # Introduce the name of the game for all players
    print("The Ancient Game of Nimm")

    # Set the starting pile at 20 stones
    pile = 20

    # Set a counter for the number of turns
    turns = 0

    # Start the game with a while loop where the exit condition is if the pile does not contain stones
    while (pile > 0):
        if pile == 1:
            # Get the player number who's turn it is
            player = call_player_number(turns)

            print(f"Player {player} please take the remaining stone.")
            pile = pile - 1
            turns += 1

        else:
            # Display the number of stones present in the pile
            print(f"There are {pile} stones left.")

            # Get the player number who's turn it is
            player = call_player_number(turns)

            # Ask player to take a stone or two
            if player == 3:
                print("Player 3 would you like to remove 1, 2 or 3 stones? ")
                output = call_gpt("Can you choose between 1, 2 or 3?")
                print(output)
            else:
                subtrahend = int(input(f"Player {player} would you like to remove 1, 2 or 3 stones? "))

            # If the value of subtrahend is greater than 2, this will require another input
            while subtrahend > 3:
                subtrahend = int(input("Please enter 1, 2 or 3: "))

            # Calculate the number of stones left in the pile after the player takes from it
            pile = pile - subtrahend

            # Increase the number of turns for every iteration of the loop
            turns += 1

            # Prints an empty row
            print("")

    # Get the player who won the game
    player = call_player_number(turns)

    # Print the winning player
    print(f"Player {player} wins!")


# This function will determine which player number's turn is it
def call_player_number(turn):
    if turn % 3 == 0:
        number = 1
    elif turn % 3 == 1:
        number = 2
    else:
        number = 3
    return number

if __name__ == "__main__":
    main()
