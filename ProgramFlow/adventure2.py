# available_exits = ['north', 'south', 'east', 'west']
# available_quits = ['quit', 'exit', 'out']
# normalized_exits = [exit.casefold() for exit in available_exits]
# normalized_quits = [q.casefold() for q in available_quits]
#
# while True:
#     exits_formatted = ', '.join(available_exits)
#     chosen_exit = input(f"Please enter available exits which are [{exits_formatted}]: ")
#     chosen_exit_caseFold = chosen_exit.casefold()
#
#     if chosen_exit_caseFold in normalized_quits:
#         print(f'you typed "{chosen_exit}"\nGAME OVER')
#         break
#     elif chosen_exit_caseFold in normalized_exits:
#         print(f'you typed "{chosen_exit}". aren\'t you glad you got out of there')
#         break
#     else:
#         print(f'you typed "{chosen_exit}" which are not [{exits_formatted}] values')



available_exits = ['north', 'south', 'east', 'west']
available_quits = ['quit', 'exit', 'out']

#normalize list once
normalized_exits = [exit.casefold() for exit in available_exits]
normalized_quits = [q.casefold() for q in available_quits]

#initialize variable
chosen_exit = ""

while chosen_exit.casefold() not in normalized_exits:
    # show menu with original casing
    exits_formatted = ', '.join(available_exits)

    # get input
    chosen_exit = input(f"Please enter available exits which are [{exits_formatted}]: ")
    chosen_exit_caseFold = chosen_exit.casefold()

    # check if user wants to quit
    if chosen_exit_caseFold in normalized_quits:
        print(f'you typed "{chosen_exit}"\nGAME OVER')
        break

    # check for invalid input
    elif chosen_exit_caseFold not in normalized_exits:
        print(f'you typed "{chosen_exit}" which are not [{exits_formatted}] values')

# if a valid exit was entered (loop condition becomes false)
else: #chosen_exit in available exits
    print(f"you typed \"{chosen_exit}\". aren't you glad you got out of there")
