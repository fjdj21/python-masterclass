# Flower and Shrub List Separator

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# go through each item in the list
for number, item in enumerate(data):
    # print out the list
    print(f"{number}: {item}")
    # normalized each item
    normalized_item = item.casefold()

    #filter if "flower" is in the item
    if "flower" in normalized_item:
        flowers.append(item)
    #filter if "shrub" is in the item
    elif "shrub" in normalized_item:
        shrubs.append(item)

print(f"{flowers}")
print(f"{shrubs}")
