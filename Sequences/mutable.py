shopping_list = [
    "milk",
    "pasta",
    "eggs",
    "spam",
    "bread",
    "rice",
]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
print(shopping_list)

shopping_list += ["cookies", "cookie mo", "new item"]
print(shopping_list)
print(id(shopping_list))

a = b = c = d = e = f = another_list
print(a)
print("Adding cream")
b.append("cream")
print(b)
print(c)
print(d)
print(e)
print(f)
print(another_list)
