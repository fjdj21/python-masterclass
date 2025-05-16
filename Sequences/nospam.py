"""
    Write code to print out all the meals in the menu, but with 'spam'
    removed.
    You can choose which approach you want to use:
        - Remove spam from each list, then print the list
        - Print out the items in each list, as long as it's not 'spam'
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
list = 0

# """This loop contains removing 'spam' from the list"""
# # Outer loop
# for meal in menu:
#     # Loop each list inside the inner loop
#     list += 1
#     # # This is for monitoring the list
#     # for index, item in enumerate(meal):
#     #     print(f"{index}, {item}")
#
#     # This is for deleting the 'spam'
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == 'spam':
#             # value = meal[index]#TODO: this is just to output what is the value of the index
#             # print(f"found the word [{value}] in index {index}")
#             # print(f"printing out the {meal}")
#             del meal[index]
#
#     print(f"list {list} | {meal} has a spam score of {meal.count('spam')}")

"""This loop is for printing out the menu when list contains 'spam'"""
# Outer loop
for meal in menu:
    # reverse index to check if the index contains 'spam'
    list += 1
    spam_free_meal = [item for item in meal if item != 'spam'] #comprehension list
    print(f"list {list} | {spam_free_meal} has a spam score of {meal.count('spam')}")
