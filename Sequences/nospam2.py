"""
    Write code to print out all the meals in the menu, but with 'spam'
    removed.
    You can choose which approach you want to use:
        - Remove spam from each list_count1, then print the list_count1
        - Print out the items in each list_count1, as long as it's not 'spam'
    You may want to write two sets of code, using both approaches

    It's up to you how you format the output. What's important is that
    you produce eight meals, all without spam.

    The output should contain something like:
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg"],
        ["egg", "bacon"],
        ["egg", "bacon", "sausage"],
        ["bacon", "sausage"],
        ["sausage", "bacon", "tomato"],
        ["egg", "bacon"]
"""

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
ruler = "-" * 50
list_count1 = 0
list_count2 = 0

# """loop to delete 'spam'"""
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

"""loop to just skip 'spam'"""
for meal in menu:
    list_count1 += 1
    print(f"list_count1: {list_count1}")
    for item in meal:
        if item != "spam":
            print(item, end=', ')
    print()

"""loop to just skip 'spam'"""
# for meal in menu:
#     list_count1 += 1
#     print(f"list_count1: {list_count1}")
#
#     # Count how many non-spam items there are
#     count = 0
#     for item in meal:
#         if item != "spam":
#             count += 1
#
#     # Print items with comma, but skip after the last
#     printed = 0
#     for item in meal:
#         if item != "spam":
#             print(item, end='')
#             printed += 1
#             if printed < count:
#                 print(', ', end='')
#     print()  # Newline after each meal


# """another approach to skip 'spam'"""
# # Outer loop
# print(ruler)
# for meal in menu:
#     # reverse index to check if the index contains 'spam'
#     list_count2 += 1
#     print(f"list_count2: {list_count2}")
#     for index in range(len(meal) -1, -1, -1):
#         if meal[index] != 'spam':
#             print(meal[index])
