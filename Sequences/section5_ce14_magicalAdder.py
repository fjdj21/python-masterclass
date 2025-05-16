"""
The Magical Adder
    For this exercise, you have to write a python program which prompts
    the user to enter three integers separated by ",".
    The user input is of the form:
    - a,b,c
    - where a, b and c are numbers.

Note that you do not have access to the keyboard on the remote server
that will be running your code. As a result, you can't use the Run code
button to execute the code.
Use the Run tests button to execute your code with our test values
(which are 7, 5, -1 and should return the answer 13).

Your program should calculate and display the result of the calculation:
a + b - c

Display the result only, don't include any extra text.

Examples:
    1. > Please enter three numbers, separated by commas: 10,11,10
        Output: 11
    2. > Please enter three numbers, separated by commas: 7,5,-1
        Output: 13

-------- LEARNING OBJECTIVE:
Develop proficiency in using input() to gather user data,
splitting strings using .split(),
and converting strings to integers to perform calculations.

"""

"""approach 1"""

numbers = input("Please enter three numbers, separated by commas: ")
# 123,123,123
allowed_characters = ['-', '.']
separators = ''
# Get all separators
for character in numbers:
    if not character.isdigit() and character not in allowed_characters:
        separators += character

#print(separators)

# check for each char if it is in separator
values = ''.join(char if char not in separators else ' ' for char in numbers).split()
#print(f"list: {values}")

# Check if we got exactly 3 values
if len(values) != 3:
    print("Error: please enter exactly three numbers separated by commas. e.g., [1,2,3]")
else:
    try:
        # try converting to integers
        for index in range(3):
            values[index] = int(values[index])

        # Perform the calculation
        calculated_value = values[0] + values[1] - values[2]
        # print(f"{calculated_value}")
        print(f"{values[0]} + {values[1]} - {values[2]} is: {calculated_value}")

    except ValueError:
        print("Error: One or more inputs were not valid integers.")

"""approach 2"""
numbers = input()
a, b, c = numbers.split(",")
print(int(a) + int(b) - int(c))

"""
1. Happy path values
    1,2,3
    1.0, 2.1, 3.1
2. More than 3 numbers
    1,2,3,4
    1.0, 2.1, 3.1, 4.1
    a, #, c
3. Negative values
    1,,12.5
"""
