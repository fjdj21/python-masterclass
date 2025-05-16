even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]


even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)


# numbers = [] # empty list to store the indexes from 'even' variable
# for i in range(1, len(even) + 1):
#     numbers.append(i)
# print(f"indexes are: {numbers}")
