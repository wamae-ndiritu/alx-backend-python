#!/usr/bin/env python3
"""
Anntonate functions
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an
    element from the input list and its corresponding length.
    """
    return [(i, len(1)) for i in lst]
