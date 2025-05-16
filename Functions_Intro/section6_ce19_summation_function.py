"""
    1. [/] Write a function to calculate the sum of all numbers passed as
        its arguments.
    2. [/] Function should be called `sum_numbers`
        [/] 2.1 Define a single variable argument (i.e. a star argument)
            that will get the values to sum.
    3. To pass in this on-line interpreter, your function must contain
        a Docstring.
        3.1. The parameters and return value must be annotated

    Test the function with the following values:
    e.g.,
        [Values]                        [Result]
        - 1, 2, 3                       # 6
        - 8, 20, 2                      # 30
        - 12.5, 3.147, 98.1             # 113.747
        - 1.1, 2.2, 5.5                 # 8.8

"""


def sum_numbers(*numbers: float) -> float:
    """
    Calculates and returns the sum of all positional arguments.

    :param numbers: A variable number of numeric arguments.
    :return: The total sum of the input numbers (int or float).
    """
    result = 0
    for num in numbers:
        result += num
    return result

def sum_numbers2(*numbers: float) -> float:
    """Calculates and returns the sum of all passed arguments
    for numbers"""

    return sum(numbers)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
