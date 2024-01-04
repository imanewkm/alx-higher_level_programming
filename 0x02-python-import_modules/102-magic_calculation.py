#!/usr/bin/python3

import os
import sys
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        add = __import__('magic_calculation_102').add
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, __import__('magic_calculation_102').add(c, i))
        return c
    else:
        sub = __import__('magic_calculation_102').sub
        return sub(a, b)
