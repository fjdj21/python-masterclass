available_parts = [
    "computer",     # 0
    "monitor",      # 1
    "keyboard",     # 2
    "mouse",        # 3
    "mouse mat",    # 4
    "hdmi",         # 5
    "dvd drive"     # 6
]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# Create a list of valid choices as strings based on the number of available parts
valid_choices = []
current_choice = "-"
# List to store the parts selected by the customer
computer_parts = []

available_parts.sort()

# Populate valid_choices with string numbers corresponding to part indices
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

# Keep looping until the user enters '0' to quit
while current_choice != '0':

    # Check if the user's input is a valid choice
    if current_choice in valid_choices:

        # Convert choice to index (1-based to 0-based)
        index = int(current_choice) - 1
        # Get the part from the list using the index
        chosen_part = available_parts[index]

        # If the part is already selected, remove it
        if chosen_part in computer_parts:
            print(f"Removing {current_choice}: {chosen_part}")
            computer_parts.remove(chosen_part)
        # Otherwise, add the selected part
        else:
            print(f"Adding {current_choice}: {chosen_part}")
            computer_parts.append(chosen_part)

        # Show the current list of selected parts
        print(f"Your list now contains: {computer_parts}")

    # If the input is not valid, show the menu again
    else:
        print("Please choose from the list below:")
        # Display available parts with numbers using enumerate
        for index, part in enumerate(available_parts):
            print(f"{index + 1}: {part}")

    # Get the next input from the user
    current_choice = input()

# Final output of selected parts
print(computer_parts)
