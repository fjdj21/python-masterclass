panagram = """The quick brown
 fox jumps\tover 
 the lazy dog"""

ruler = "-" * 50

words = panagram.split()
print(words)
print(ruler)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(','))
print(ruler)

# values = ''.join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
print(generated_list)
values = ''.join(generated_list)
print(values)

values_list = values.split()
print(values_list)

""" mini challenge
    Use a for loop to produce a list of ints, rather than strings:
    You can either:
        - Modify the contents of the 'values_list' list in place, or
        - create a new list of ints
"""

# modify each content to int without using a new list of int
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(f"int values using for loop:\t\t{values_list}")

# produce a new list of ints
int_values_list = [int(i) for i in values_list ] #comprehension list
print("Comprehension list")
print(f"producing a new list of ints:\t{int_values_list}")

# ordinary for loop
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print("Ordinary for loop")
print(f"producing a new list of ints:\t{int_values_list}")
print(ruler)

"""
    ### mini challenge 2
    Your Tasks:
        1. Filter out any items that are not pure numbers (you can use .isdigit() for this).
        2. Convert the remaining strings into integers.
        3. Store the result in a new list called cleaned_ints and print it.
    Expected Output:
        [123, 456, 789, 0, 321]
"""

raw_data = ['123', '-', '456', 'abc', '789', '0', 'xyz', '321']
cleaned_ints = []

# check if the list is digit
for item in raw_data:
    if item.isdigit():
        cleaned_ints.append(item)

print(cleaned_ints) # str

# convert each item to int
for index in range(len(cleaned_ints)):
    cleaned_ints[index] = int(cleaned_ints[index])

print(cleaned_ints) # int

""" another way to have this in one go """
raw_data2 = ['123', '-', '456', 'abc', '789', '0', 'xyz', '321']
cleaned_ints2 = [int(item) for item in raw_data2 if item.isdigit()]
print(cleaned_ints2)
