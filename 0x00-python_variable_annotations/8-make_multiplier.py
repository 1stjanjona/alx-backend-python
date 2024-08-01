#!/usr/bin/env python3
'''8-make_multiplier.py file'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''return multiplies of float by multiplier'''
    def multiplier_function(m: float) -> float:
        '''multiplier of two floats'''
        return m * multiplier
    return multiplier_function
