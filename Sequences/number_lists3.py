empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even , odd]
print(numbers)

#outer loop
for number_list in numbers:
    print(number_list)
    # inner loop
    for value in number_list:
        print(value)
