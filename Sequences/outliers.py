data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

print(f"length starting from 0: {len(data) - 1}")

# #   deletes 2 index
# #   - delete starting from index 0 up to and not including index 2
# #   note that the total indexes are also changed from 17 to 15
# del data[0:2]
# print(data)
# print(f"length starting from 0: {len(data) - 1}")
# del data[14:]
# print(data)
# print(f"length starting from 0: {len(data) - 1}")

min_valid = 100
max_valid = 200

# don't do this, since when deleting a data from a mutable object
# the index changes, e.g., from 17 - 16
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)
