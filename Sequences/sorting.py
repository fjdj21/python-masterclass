pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
print(f"original {numbers}")
sorted_numbers = sorted(numbers)
print(f"sorted: {sorted_numbers}")
print(f"original: {numbers}")

# another_sorted_numbers = numbers.sort()
numbers.sort()
print(f"sort {numbers}")
# print(f"another sorted: {another_sorted_numbers}")

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold) #key= ... sort as an argument with case insensitivity
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
