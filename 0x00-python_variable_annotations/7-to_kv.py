#!/usr/bin/env python3
'''7-to_kv.py file'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return tuple of two different types'''
    return (k, float(v ** 2))
