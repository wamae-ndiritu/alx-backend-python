#!/usr/bin/env python3
"""
Defines function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    return multiplier_func
