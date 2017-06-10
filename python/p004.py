#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


def is_palindrome(string):
    """
    Check if a string is palindrome
    :param string: 
    :return: True if string is palindrome, False otherwise.
    """
    for i in range(0, len(string)/2):
        if string[i] != string[-i-1]:
            return False
    return True


def get_3_digits_palindromes():
    palindromes = []
    for factor_i in range(999, 99, -1):
        for factor_j in range(999, factor_i-1, -1):
            number = factor_i * factor_j
            number_str = "{0}".format(number)
            _is_palindrome = is_palindrome(number_str)
            if _is_palindrome:
                palindromes.append(number)
    return palindromes


if __name__ == "__main__":
    print("Finding the largest palindrome made from the product of two 3-digit numbers")
    print(max(get_3_digits_palindromes()))
