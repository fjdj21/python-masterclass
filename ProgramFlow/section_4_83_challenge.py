"""
Challenge:
- Write a program to:
    - [/] print a number of options
    - [/] allow the user to select an option from the list.
        - [/] the options from the list should be numbered from 1 to 9,
        although you can use less than 9 options if you want.
        - [/] at least 4 options
    - [/] the program should continue looping, allowing the user to choose
    one of the options each time round.
    - [/] The loop should only terminate when the user chooses 0.
    - [/] if the user makes a valid choice, the program should print a
    short message
        - [/] The message should include the value that they typed
    - [/] Don't print a different message for each choice - the only thing
    that should change is the number they typed.
    - Although you could print out the description, I want to show you
    a much better way of doing that, later.
    - We're keeping this simple, because there are still lots of things
    we haven't covered yet.
    - [/] If their choice isn't one of the options in the menu, nothing
    should be printed (although you will see their input on the screen)
    - [/] As an optional extra, modify the program so that the menu is prin-
    ted again, if they choose an invalid option
    - Be careful with that one: you may start off by duplicating the co-
    de to print the menu, but it's possible to write the program without
    duplicating the print lines.

Example:
    Please choose your option from the list below:
    1. Learn Python
    2. Learn Java
    3. Go swimming
    4. Have dinner
    5. Go to bed
    0. Exit
"""

options = ["exit", "operator", "odin", "vandal", "phantom",
           "guardian", "bulldog", "spectre", "stinger", "sheriff", "marshal"]

user_input = "" # initialize

while True:
    # list down the options available when going back
    print("Please choose your option from the list below:")
    for index, option in enumerate(options[1:], start = 1):
        print(f"{index}. {option.capitalize()}")
    print(f"{options.index("exit")}. {options[0].capitalize()}")
    print("-" * 80)

    # ask for user input
    user_input = input("Enter your choice here: ")

    # check if input is not a digit
    if not user_input.isdigit():
        print(f"You typed '{user_input}', please type values from 1 to {len(options)-1}")
        print(f"If you want to quit, type {options.index("exit")}")
        print("-" * 80)
        continue # restart the loop

    # if digit
    user_choice = int(user_input) # store as int

    if user_choice == options.index(options[0]):
        # exit of loop if user typed 0
        print(f"You typed '{user_input}' - {options[user_choice].capitalize()}. Exiting...")
        break
    if user_choice >= len(options):
        # if user typed more than the list values e.g., 11
        print(f"Choice out of range, choose again")
        print("-" * 80)
        continue
    else:
        # choice within range
        print(f"You chose {user_choice}. {options[user_choice].upper()}, what a nice choice")
        print("-" * 80)
