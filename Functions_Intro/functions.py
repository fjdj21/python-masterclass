def multiply(x, y):
    result = x * y
    return int(result)


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
