"""
Creating a Python Function to Calculate Factorials with Docstrings

    The factorial of a number is the product of all the values from 1 to
    the number, inclusive.

    Thus 4 factorial, which is written as 4!, is calculated as
        1 * 2 * 3 * 4 = 24

    5! is
        1 * 2 * 3 * 4 * 5 = 120

    The convention is that 0! = 1 (not zero, as you might expect).

    Write a function called factorial, that will return the factorial
    of the number passed as its argument.

    You must include a Docstring, and function annotations,
    in your function.

    Use a for loop to call your factorial function, to print out the
    first 36 factorials (0 to 35). Your results should be
"""

""" PSEUDOCODE for factorial
    
    FUNCTION factorial(n: INTEGER) RETURNS INTEGER
        SET result TO 1
        FOR i FROM 1 TO n DO
            SET result TO result * i
        END FOR
        RETURN result
    END FUNCTION

"""
def factorial(n: int) -> int:
    """returns the factorial of the given number `n`."""
    if n <= 1:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


""" PSEUDOCODE for the loop
    START
        FOR i FROM 0 to 35 DO
            DISPLAY "{i} {factorial(i)}"
    END 
"""

# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
#
#     return result

for i in range(3):
    print(i, factorial(1))
