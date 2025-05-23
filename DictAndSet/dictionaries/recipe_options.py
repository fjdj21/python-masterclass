from z_debuggers import banner, ruler

recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
    ],
}

recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
    },
}


banner("Using tuples")
# using tuples
for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients:  # ingredients is a tuple
        print(ingredient, quantity, sep=', ')


banner("using dictionary")
# using a dictionary
for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items():  # ingredients is a dict
        print(ingredient, quantity, sep=', ')

ruler()
