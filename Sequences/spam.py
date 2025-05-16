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
sub_item = []

for meal in menu:
    if "spam" not in meal:
        print(ruler)
        print(f"this is the list that don't contain spam")
        print(meal)
        print(ruler)
        for item in meal:
            sub_item.append(item)
            print(item)
    else:
        print(ruler)
        print(f"{meal} has a spam score of {meal.count('spam')}")
