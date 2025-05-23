from z_debuggers import banner, ruler, COLORS

d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# banner('from-keys method')
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)
#
# banner('keys method')
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)

# banner('Update method for efficient merging')
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }
#
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# banner('update `d` dictionary with the tuple list generated by enumerate')
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

banner('values method - a view objects (e.g., .keys, .values, .items')
v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

banner('takes up lots of memories')
keys = list(d.keys())
values = list(v)    # => list(d.values)
for val in values:
    if val == "four":
        index = values.index("four")
        key = keys[index]
        print(f"{d[key]} was found with the key {key}")

banner('this only return once - takes up lots of memories as well')
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

banner('More efficient way when searching to large number of dict`s')
for key, value in d.items():
    if value == 'four':
        print(f"{d[key]} was found with the key {key}")
