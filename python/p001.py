#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


def multiples_of_3_and_5(below_limit):
    for num_i in range(3, below_limit):
        if num_i % 3 == 0 or num_i % 5 == 0:
            yield num_i


if __name__ == "__main__":
    print(sum(multiples_of_3_and_5(below_limit=1000)))
