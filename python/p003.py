#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import sys


def get_factors(number):
    factors = []
    factor_i = 2
    max_possible_factor = int(number / 2)
    number_i = number
    while number_i > 1 and factor_i <= max_possible_factor:
        if number_i % factor_i == 0:
            number_i /= factor_i
            factors.append(factor_i)
            if number_i == factor_i * factor_i:
                break
        factor_i += 1
    return factors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Compute the largest prime factor of a number")
        print("User ./p003.py <number>")
    else:
        _number = int(sys.argv[1])
        print("Checking largest prime of {0}".format(_number))
        print(max(get_factors(_number)))
