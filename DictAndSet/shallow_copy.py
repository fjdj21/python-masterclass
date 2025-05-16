from z_debuggers import banner, ruler
banner('immutable')
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# doesn't matter, it is the same list whether changing things/animals
things = animals
animals["teddy"] = "toy"
# things["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])

banner('using copy method')
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])

banner('MUTABLE')
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

things = animals.copy()

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
