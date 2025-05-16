from dictionaries.contents_quantities import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.get("beans", 0)
print(f"beans: {beans_quantity}")
