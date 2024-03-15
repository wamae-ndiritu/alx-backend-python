#!/usr/bin/env python3
"""
Augmenting the code with the correct duck-typed annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None
    """
    if lst:
        return lst[0]
    else:
        return None
