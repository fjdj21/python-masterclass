ruler = "-" * 50
name = "Tim"
age = 10

# print(*objects, sep=' ', end='\n', file=None, flush=False)

print(name, age, "Python", 2020)  # *objects
# Tim 10 Python 2020
"""
    this means that multiple objects can be called inside the print-
    function that is separated with comma
"""

print(name, age, "Python", 2020, sep=", ")  # sep=
# Tim, 10, Python, 2020
print(name + str(age) + "Python" + str(2020), sep=", ")
# Tim10Python2020
"""
    on line 6, the default separator when calling multiple objects is-
    that it is separated by sep=' ' on default
    
    in here, we call each object, once it is printed out the separator
    displayed is now set to '<,><space>'
"""
print(ruler)
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

list_count1 = 0

"""loop to just skip 'spam' using keyword argument: end="""
for meal in menu:
    list_count1 += 1
    print(f"list_count1: {list_count1}")
    for item in meal:
        if item != "spam":
            print(item, end=', ')
    print()
