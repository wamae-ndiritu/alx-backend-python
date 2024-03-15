#!/usr/bin/env python3
"""
Adding type annotations
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely gets a value from a dictionary.
    Returns the value associated with the given key if present,
    otherwise returns the default value (or None if not specified).
    """
    if key in dct:
        return dct[key]
    else:
        return default
