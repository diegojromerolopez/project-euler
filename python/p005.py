#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


def get_smallest_divisible_number_brute_force(max_factor):
    """
    Get the smallest divisible number by all [1..max_factor] numbers by brute force.
    """
    number_i = max_factor
    while True:
        divisible = True
        for factor_i in range(1, max_factor+1):
            if number_i % factor_i > 0:
                divisible = False
                break
        if divisible:
            return number_i
        number_i += 1


def least_common_multiple(a, b):
    """
    Get the least common multiple of a and b.
    """
    a, b = min(a, b), max(a, b)

    if b % a == 0:
        return b

    found = False
    number_i = 1
    multiple_i = a
    while not found:
        if multiple_i % b == 0:
            return multiple_i
        number_i += 1
        multiple_i = a * number_i


def get_smallest_divisible_number(max_factor):
    """
    Get the smallest divisible number by all [1..max_factor] numbers by using the LCM (least common multiple).
    """
    res = 1
    for factor_i in range(1, max_factor + 1):
        res = least_common_multiple(res, factor_i)
    return res


if __name__ == "__main__":
    print("Finding the smallest positive number that is evenly divisible by all of the numbers from 1 to 20")
    print(get_smallest_divisible_number(max_factor=20))
