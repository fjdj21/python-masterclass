from dictionaries.contents_quantities import recipes

"""
    Simple Deep Copy Challenge

    Write a function that takes a dictionary as an argument, and
    returns a deep copy of the dictionary.

    You're going to write your own function, to do a similar job to the
    `deepcopy` function that we've just used. But you'll do it
    `without` using the `copy` module.

    Your function will be a lot simpler than deepcopy. It only has to
    cope with 1 level of contained objects. It should be able to
    successfully copy dictionaries like our animals or recipes
    dictionaries

    It doesn't have to handle dictionaries that contain objects that
    also contains objects. That's much too difficult at this stage.

    The basic approach will be to create a new, empty dictionary
    Next, iterate over the keys and values of the dictionary that's
    being copied.

    For each key, copy the value, then add the copy of the value to the
    new dictionary.

    Your function only has to handle values that are dictionaries or lists.
    Both of those objects have a copy method.

"""

def my_deepcopy(data: dict) -> dict:
    new_data = {}
    for key, value in data.items():
        new_value = value.copy()
        new_data[key] = new_value

    return new_data

    # # Approach 2
    # for key, value in data.items():
    #     if isinstance(value, (list, dict)):
    #         new_data[key] = value.copy()
    #     else:
    #         new_data[key] = value
    # return new_data

# recipes_copy = my_deepcopy(recipes)
# recipes_copy["Butter chicken"]["ginger"] = 300
# print(recipes_copy["Butter chicken"]["ginger"])
# print(recipes["Butter chicken"]["ginger"])
# print(recipes)
# print(recipes_copy)
