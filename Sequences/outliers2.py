data    = [     4,   5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360 ]
# index         0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17
# -index        -18, -17, -16, -15, -14, -13, -12, -11, -10,  -9,  -8,  -7,  -6,  -5,  -4,  -3,  -2,  -1
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

print(f"length starting from 0: {len(data) - 1}")

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
        if value >= min_valid:
                stop = index
                break
print(stop) # for debugging
print(f"before:\t{data}")
del data[:stop]
print(f"after:\t{data}")
print(f"length starting from 0: {len(data) - 1}")

# process the high values in the list
start = 0
for index in range(len(data) -1, -1, -1):
        if data[index] <= max_valid:
                start = index + 1
                break
print(start)
print(f"before:\t{data}")
del data[start:]
print(f"after:\t{data}")
print(f"length starting from 0: {len(data) - 1}")
