#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num-1) + fib(num-2)


def fibonacci_sequence(limit):
    num_i = 0
    fib_num_i = 1
    while fib_num_i < limit:
        fib_num_i = fib(num_i)
        yield fib_num_i
        num_i += 1


if __name__ == "__main__":
    fibonacci_numbers = fibonacci_sequence(4000000)
    fibonacci_sequence_sum = sum(filter(lambda item: item % 2 == 0, fibonacci_numbers))
    print(fibonacci_sequence_sum)
