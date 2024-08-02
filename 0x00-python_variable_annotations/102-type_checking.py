#!/usr/bin/env python3
'''102-type_checking.py file'''
from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''apply any necessary changes'''
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
