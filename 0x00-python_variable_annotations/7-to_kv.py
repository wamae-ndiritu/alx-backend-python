#!/usr/bin/env python3
"""
Define function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tupple where the first element is the string k
    and the second element is the square of v.
    """
    return (k, float(v * v))
