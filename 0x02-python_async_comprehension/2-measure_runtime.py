#!/usr/bin/env python3
"""
Measure runtime
"""
import asyncio
from typing import List
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four
    times in parallel using asyncio.gather and measures
    the total runtime
    """
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    return end_time - start_time
