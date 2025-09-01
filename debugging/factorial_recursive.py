#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
        n (int): The number to compute the factorial of.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of n.

    Example:
        factorial(4) -> 24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the first command-line argument, convert it to int, and compute factorial
f = factorial(int(sys.arg
