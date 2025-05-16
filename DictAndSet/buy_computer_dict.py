available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "mouse mat",
    "6": "hdmi",
    "7": "dvd drive",
}

current_choice = None
computer_parts = {}  # create an empty dictionary

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
            # adding an item in dictionary:
            # vehicles["starfighter"] = "Lockheed F-104"
            # variable['key'] = 'value'

        print(f"Your dictionary now contains: {computer_parts}")

    else:
        print("Please choose from the list below:")
        # Iterate Dict available parts
        for num, part in available_parts.items():
            print(num, part, sep=": ")
        print("0: to finish")

    current_choice = input("> ")
