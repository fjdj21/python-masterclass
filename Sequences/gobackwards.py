data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    reversed_index = index - (len(data))
    print(f"index\\reversed: {index:}\t\\\t{reversed_index:>3},\tvalue: {value}")

for index in range(len(data)-1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        value = data[index]
        print(f"found outside min/max at index: {index} with value of {value}, {data}")
        del data[index]
        print(f"data adjusted: {data}")

print(data)
