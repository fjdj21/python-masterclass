computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

# Using enumerate to get both the index and value from the list
for index, part in enumerate(computer_parts):
    print(f"{part} - {index}")

print()

# Accessing the 3rd item (index 2) from the list
print(computer_parts[2])  # Output: keyboard

# Slicing the list from index 0 up to (but not including) index 3
print(computer_parts[0:3])  # Output: ['computer', 'monitor', 'keyboard']

# Accessing the last item in the list using negative indexing
print(computer_parts[-1])  # Output: mouse mat
