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

# Take input from the user
user_input = input("Please enter three numbers, separated by commas: ")
# Split the given input string into 3 parts
string_tokens = user_input.split(",")

# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))

# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# result = int_tokens[0] + int_tokens[1] - int_tokens[2]

# Output the result
print(result)
