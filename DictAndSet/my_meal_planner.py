from dictionaries.contents_quantities import pantry, recipes
from z_debuggers import banner, ruler, COLORS

def display_menu(data: dict) -> None:
    """Displays numbered menu items"""
    banner("Menu", "*")
    for key, value in data.items():
        print(f"{key} - {value}")

def check_pantry(ingredient: str, required_quantity: int) -> None:
    if required_quantity <= quantity_in_pantry:
        # print(f"\t{ingredient} {required_quantity} OK")
        return 0
    else:
        quantity_to_buy = required_quantity - quantity_in_pantry
        print(f"\tYou need to buy {RED}{quantity_to_buy}{RESET} of {ingredient}")
        return quantity_to_buy

def add_to_shopping_list(item: str, quantity: int, data: dict) -> None:
    # option 1
    data[item] = data.get(item, 0) + quantity
    # option 2
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity

    # option 3
    # data[item] = data.setdefault(item, 0) + amount

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


recipe = {str(index) : meal for index, meal in enumerate(recipes, start=1)}
user_input = '-'

shopping_list = {}

while user_input != "0":

    display_menu(recipe)
    print("0 - Exit")
    ruler('*')

    print(f"{CYAN}Choose a recipe number (1 to {len(recipe)}), "
          f"or 0 to exit:{RESET}")
    user_input = input("> ")

    if user_input in recipe:
        # Store selected recipe
        selected_recipe = recipe[user_input]
        print(f"You have selected {selected_recipe}")

        # Get ingredients from recipes
        ingredients = recipes[selected_recipe]
        print(f"Checking ingredients...")
        print(ingredients) #TODO: to remove after testing

        # Loop through ingredients:
        for food_item, quantity_needed in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)

            # Check if the quantity required
            if quantity_in_pantry < quantity_needed:
                to_buy =  quantity_needed - quantity_in_pantry
                print(f"\tYou need to buy {to_buy} of {food_item}")
                # Add to shopping list
                add_to_shopping_list(food_item, to_buy, shopping_list)

display_shopping_list(shopping_list)
