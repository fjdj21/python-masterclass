"""
Challenge:
    Even or Odd Numbers within a Specified Range

    In this coding exercise, you have to write a function named sum_eo
    with the following parameters:

    n: a positive number
    t: a str


    If t has the value 'e', the function should return the sum of all
        even natural numbers less than n.

    Else if t has the value 'o', the function should return the sum of
        all odd natural numbers less than n.

    For any other values of t return -1.

    Examples:
    1. sum_eo(10, 'e') should return 20, since 2 + 4 + 6 + 8 = 20
    2. sum_eo(7, 'o') should return 9, since 1 + 3 + 5 = 9
    3. sum_eo(11, 'spam') should return -1
"""

def sum_eo(n, t):
    n = int(n)
    even = 0
    odd = 0

    if t == 'e':
        for i in range(1, n):
            if (i % 2) == 0:
                even += i
        return even

    elif t == 'o':
        for i in range(1, n):
            if (i % 2) != 0:
                odd += i
        return odd
    return -1


def sum_eo2(n,t):

    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
