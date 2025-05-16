data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
"""remove end values"""
# data    = [     4,   5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191 ]
"""remove beginning values"""
# data    = [     104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360 ]
"""remove both beginning and end values"""
# data    = [     104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191 ]
"""add data outside min and max"""
# data    = [     1041, 1051, 1101, 1201, 1301, 1301, 1501,
#                 1601, 1701, 1831, 1851, 1871, 1881, 1911]
"""blank data"""
# data    = []


min_valid = 100
max_valid = 200
ruler = "-" * 10

# for index, value in enumerate(data):
#     reversed_index = index - (len(data))
#     print(f"index\\reversed: {index:}\t\\\t{reversed_index:>3},\tvalue: {value}")

# for index in range(len(data)-1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         value = data[index]
#         print(f"found outside min/max at index: {index} with value of {value}, {data}")
#         del data[index]
#         print(f"data adjusted: {data}")

# print(data)

print(f"{ruler}reversed function(){ruler}\n")

top_index = len(data) -1
for index, value in enumerate(reversed(data)):
    orig_index = top_index - index
    if value < min_valid or value > max_valid:
        print(f"found outside min/max at index:\t[{orig_index}] with value of\t[{value}]")
        print(f"orig data list:\t{data}")
        del data[orig_index]
        print(f"adjusted:\t\t{data}")

print(ruler * 5)
print(data)
