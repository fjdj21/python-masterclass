# number = "9,223;372:036 854,775;807"
# separators = number[1::4]
# print(separators)
#
# # values = "".join(char if char not in separators else " " for char in number).split()
# # print(values)
# # print([int(val) for val in values])
# #
# # words = ["I", "love", "dogs"]
# # sentence = ' '.join(words).split()
# # print(sentence)

#number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

# Get all separators (non-digit characters) and add them to the 'separators' string
for character in number:
    if not character.isdigit():
        separators += character

print(separators)

# Join each character:
# - If the character is NOT a separator (i.e., a number), keep it.
# - If it IS a separator (e.g., ',', ';', etc.), replace it with a space.
# Result: "9 223 372 036 854 775 807"
# Then, split this string into a list by spaces -> ['9', '223', '372', '036', '854', '775', '807']
values = ''.join(char if char not in separators else ' ' for char in number).split()
print(f'values after joining then split: {values}')

# Convert each value (currently a string) into an integer
# e.g., '9' -> 9, '223' -> 223, etc.
print(f'converts each value to int: {[int(val) for val in values]}')
print(f'The sum value of these are: {sum([int(val) for val in values])}')
