# Outer loop: This loop controls the "times" part (1 to 12)
for i in range(1, 13):  # i will take values from 1 to 12
    # Inner loop: This loop controls the multiplier (1 to 12)
    for j in range(1, 13):  # j will take values from 1 to 12
        # For each pair (i, j), print the multiplication result
        # {j:<2} → left-align j in 2 spaces
        # {i:<2} → left-align i in 2 spaces
        # {i * j:<3} → left-align the result of i*j in 3 spaces
        print(f'{j:<2} times {i:<2} is {i * j:<3}')

    # After finishing the inner loop (i.e., after showing 1–12 multipliers for 1 number),
    # print a line of 80 hyphens to separate the "times tables" clearly
    print('-' * 80)


"""This is just another challenge"""
# # Ask the user up to what number they want the multiplication table
# max_number = int(input("Enter the maximum number for multiplication table: "))
#
# # Print the header row first (1 to 12)
# print("    ", end="")  # 4 spaces for the top-left corner
# for header in range(1, max_number + 1):
#     print(f"{header:>4}", end="")  # Right-align headers with 4 spaces
# print()  # New line after header row
#
# # Print a separator line below the header
# print("    " + "-" * (4 * (max_number + 1) - 4))
#
# # Outer loop: Rows for 1 to 12
# for i in range(1, max_number + 1):
#     # Print the leftmost column (the multiplier number)
#     print(f"{i:<3}|", end="")  # Left-align multiplier, then vertical bar
#
#     # Inner loop: Multiplying current i with j from 1 to 12
#     for j in range(1, max_number + 1):
#         print(f"{i * j:>4}", end="")  # Right-align each product in 4 spaces
#     print()  # New line after each row
