#!/usr/bin/env python3
"""
Defines a function to measure the runtime
"""
from time import time
import asyncio
from typing import List
from asyncio import Task


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """"
    Measure the total execution for wait_n(n, max_delays)
    and return total_time / n.
    """
    start_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time()
    total_time = end_time - start_time
    return total_time / n
