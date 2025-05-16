#imports here
from z_debuggers import ruler, banner

def multiply(x, y):
    result = x * y
    return int(result)


def multiply(x: float, y: float) -> float:
    """
    Multiply two values and return the result as an integer.

    :param x: (int or float): The first number to multiply.
    :param y: (int or float): The second number to multiply.
    :return: The result of x multiplied by y, converted to an integer.
    """
    result = x * y
    return int(result)


def is_palindrome(string: str) -> bool:
    """
    Check if a given string is a palindrome (ignores case).

    A palindrome is a word or phrase that reads the same forwards and
    backwards.

    :param string: The string to check
    :return: bool: `True` if the string is a palindrome, `False`
    otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome by ignoring spaces and punctation.

    Only alphanumeric characters are considered, and case is ignored.

    :param sentence: The sentence to check.
    :return: bool: `True` if the cleaned sentence is a palindrome,
    `False` otherwise.
    """
    """Approach 1"""
    # # iterate each character and filter if that char is an alnum()
    # s = ''.join(char for char in sentence if char.isalnum())
    #
    # return is_palindrome(s)

    """Approach 2"""
    # use a for loop to iterate each character in a sentence
    string = "" # initialize, this is where each character will be stored
    for char in sentence:
        if char.isalnum():
            string += char

    return is_palindrome(string) # called is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None

    for f in range(n - 1):
        result = n_minus2 + n_minus1 # 1 + 0 = 1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

def fibonacci_2(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_2(n - 1) + fibonacci_2(n - 2)
        return result

def my_fibonacci(n: int) -> int:

    if 0 <= n <= 1:
        return n

    a, b = 0, 1

    result = None

    for f in range(n - 1):
        result = a + b
        a = b
        b = result

    return result

    # n = 0 | = a(0) # skip
    # n = 1 | = b(1) # skip
    # n = 2 | = result(a + b) [1] | a = 1, b = 1
    # n = 3 | = result(a + b) [2] | a = 1, b = 2
    # n = 4 | = result(a + b) [3] | a = 2, b = 3
    # n = 5 | = result(a + b) [5] | a = 3, b = 5

# # Test data:
# #   - A man,    a plan,    a canal: Panama!
# #   - babcvsda21
#
# word = input("Please enter a word to check: ")
# # Check if input is not a string (e.g., #@!, 123)
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome")
#
# answer = multiply(18, 3)
# print(answer)

# [a][b] = [c]
#

while True:
    iterator = input("Please enter a number: ")

    if iterator == 'q':
        print(f"you typed '{iterator}', exiting this loop")
        break

    if iterator == '0':
        print(f"This is not a valid range for fibonacci, try again")
    else:
        try:
            iterator = int(iterator)

            for i in range(iterator):
                print(f"#{i}, {my_fibonacci(i)}")

        except ValueError:
            print("Please input a valid number (e.g., 1)")

p = is_palindrome()
p = palindrome_sentence()
p = fibonacci()
