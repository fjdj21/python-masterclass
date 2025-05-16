from dictionaries.contents_quantities import pantry, recipes
from z_debuggers import ruler, banner, COLORS

# def add_shopping_item(data: list, item: str, amount:int) -> None:
#     """Add a tuple containing `item` and `amount` to `data` list"""
#     data.append((item, amount))

def add_shopping_item_dict(data: dict, item: str, amount:int) -> None:
    """Add key/value pairs `item' and `amount` to `data` dictionary"""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount

def display_shopping_list(data: dict) -> None:
    if data:
        print(f"\n{BOLD}Shopping List:{RESET}")
        for item, quantity in data.items():
            print(f"- {item}: {quantity}")
    else:
        print("\nNo items needed from the store!")


# Extract constants from the dictionary for direct use
BLACK = COLORS["BLACK"]
RED = COLORS["RED"]
GREEN = COLORS["GREEN"]
YELLOW = COLORS["YELLOW"]
BLUE = COLORS["BLUE"]
MAGENTA = COLORS["MAGENTA"]
CYAN = COLORS["CYAN"]
WHITE = COLORS["WHITE"]
RESET = COLORS["RESET"]
BOLD = COLORS["BOLD"]
UNDERLINE = COLORS["UNDERLINE"]
REVERSE = COLORS["REVERSE"]

# ruler()
# print(pantry)
# print(recipes)
# ruler()

# banner("1 Liner Code", '*')
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# print(display_dict)
# ruler()

banner("NORMAL WAY OF DISPLAYING THE LIST")

display_dict = {}
# get the recipes dict to be in a new dictionary
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

# shopping_list = []
# # Create a shopping list

dict_shopping_list = {}
# Create a dictionary list

while True:
    # Display a menu of the recipe
    print("Please choose your recipe: ")
    ruler('-',default=False)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    # Ask for user input
    choice = input(": ")

    # Quit the loop if 0
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        #retrieve the list from the selected recipe dictionary
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        # iterate on each ingredients
        for food_item, required_quantity in ingredients.items():
            # get quantity from pantry, otherwise display 0
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            # if quantity_in_pantry <= required_quantity:
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {RED}{quantity_to_buy}{RESET} of {food_item}")
                # Add the items to a shopping_list
                add_shopping_item_dict(dict_shopping_list, food_item, quantity_to_buy)

display_shopping_list(dict_shopping_list)
