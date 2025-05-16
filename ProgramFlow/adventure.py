# available_exits = ['north', 'south', 'east', 'west']
# available_quits = ['quit', 'exit', 'out']
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     exits_formatted = ', '.join(exit for exit in available_exits)
#     chosen_exit = input(f"Please enter available exits which are [{exits_formatted}]: ").casefold()
#     if chosen_exit in available_quits:
#         print(f'you typed "{chosen_exit}"\nGAME OVER')
#         break
#     elif chosen_exit not in available_exits:
#         print(f'you typed "{chosen_exit}" which are not [{exits_formatted}] values')
#     else:
#         print("aren't you glad you got out of there")


###

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    quotient = i // 11
    remainder = i % 11
    product = quotient * 11  # correct product, based on how many 11s fit
    if i > 0 and i % 11 == 0:
        break
    print(f'{i:<2} % 11 is {remainder:<3} - ' +
          f'{{{quotient} x 11 = {product:>2}, quotient: {quotient}, remainder: {remainder}}}')
# 0  % 11 is 0   - {0 x 11 =  0, quotient: 0, remainder: 0}
# 7  % 11 is 7   - {0 x 11 =  0, quotient: 0, remainder: 7}
# 14 % 11 is 3   - {1 x 11 = 11, quotient: 1, remainder: 3}
# 21 % 11 is 10  - {1 x 11 = 11, quotient: 1, remainder: 10}
# 28 % 11 is 6   - {2 x 11 = 22, quotient: 2, remainder: 6}
# 35 % 11 is 2   - {3 x 11 = 33, quotient: 3, remainder: 2}
# 42 % 11 is 9   - {3 x 11 = 33, quotient: 3, remainder: 9}
# 49 % 11 is 5   - {4 x 11 = 44, quotient: 4, remainder: 5}
# 56 % 11 is 1   - {5 x 11 = 55, quotient: 5, remainder: 1}
# 63 % 11 is 8   - {5 x 11 = 55, quotient: 5, remainder: 8}
# 70 % 11 is 4   - {6 x 11 = 66, quotient: 6, remainder: 4}
# 77 % 11 is 0   - {7 x 11 = 77, quotient: 7, remainder: 0}
# 84 % 11 is 7   - {7 x 11 = 77, quotient: 7, remainder: 7}
# 91 % 11 is 3   - {8 x 11 = 88, quotient: 8, remainder: 3}
# 98 % 11 is 10  - {8 x 11 = 88, quotient: 8, remainder: 10}
print('-' * 80)

for i in range(0, 21):
    quotient = i // 3
    remainder = i % 3
    product = quotient * 11
    if i % 3 == 0 or i % 5 == 0:
        continue #skip
    print(f'{i:<2} % 3 is {remainder:<3} - ' +
          f'{{{quotient} x 3 = {product:>2}, quotient: {quotient}, remainder: {remainder}}}')
