#!/usr/bin/python3
"""
Module calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """function to handle the minimum operation"""
    if n <= 1:
        return 0

    operation = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operation += factor
            n = n // factor
        factor += 1
    return operation
