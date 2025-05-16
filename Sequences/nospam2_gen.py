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

for meal in menu:
    list_count1 += 1
    print(f"list number: #{list_count1}")
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
