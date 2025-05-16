from z_debuggers import ruler, banner


"""
    Create Docstrings for the three functions written from
    `functions.py` module

    Check your Docstrings by using `Ctrl-Q`, to make sure they're
    formatted correctly, and provide all the information someone
    would need to use the functions

    Note: make sure you test your functions, after adding the Docstrings
    , to make sure you haven't broken anything
"""


def multiply(x, y):
    """
    Multiply two values and return the result as an integer.

    :param x: (int or float): The first number to multiply.
    :param y: (int or float): The second number to multiply.
    :return: The result of x multiplied by y, converted to an integer.
    """
    result = x * y
    return int(result)


def is_palindrome(string):
    """
    Check if a given string is a palindrome (ignores case).

    A palindrome is a word or phrase that reads the same forwards and
        backwards.

    :param string: The string to check
    :return: bool: True if the string is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome by ignoring spaces and punctation.

    Only alphanumeric characters are considered, and case is ignored.

    :param sentence: The sentence to check.
    :return: bool: True if the cleaned sentence is a palindrome, False otherwise.
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


# # Test data:
# #   - A man,    a plan,    a canal: Panama!
# #   - babcvsda21

banner("is_palindrome")

word = input("Please enter a word to check: ")
# Check if input is not a string (e.g., #@!, 123)
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

banner("palindrome_sentence")

word = input("Please enter a word to check: ")
# Check if input is not a string (e.g., #@!, 123)
if palindrome_sentence(word):
    print(f"{word} is a palindrome")
else:
    print(f"'{word}' is not a palindrome")

answer = multiply(18, 3)
print(answer)
