available_parts = {
    "1":   "computer",
    "2":   "monitor",
    "3":   "keyboard",
    "4":   "mouse",
    "5":   "mouse mat",
    "6":   "hdmi",
    "7":   "dvd drive",
}

current_choice = None # user choice
computer_parts = [] # empty to list to store the chosen parts

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        # Remove if chosen part wants to be removed
        if chosen_part in computer_parts:
            print(f"Removing - {chosen_part}")
            computer_parts.remove(chosen_part)
        else: # Add if not yet existing
            print(f"Adding - {chosen_part}")
            computer_parts.append(chosen_part)

        # Show the current list of selected parts:
        print(f"Your list now contains: {computer_parts}")

    else:
        print("Please choose from the list below:")
        # Iterate Dict available parts
        for num, part in available_parts.items():
            print(num, part, sep=": ")
        print("0: to finish")

    current_choice = input("> ")
