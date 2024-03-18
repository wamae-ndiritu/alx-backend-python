#!/usr/bin/env python3
"""
Executing multiple coroutines at the same
time with async
"""
import asyncio
from typing import List
from random import uniform
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.
    """
    tasks: List[Task] = [
            asyncio.create_task(wait_random(max_delay))
            for _ in range(n)
            ]
    delays: List[float] = await asyncio.gather(*tasks)
    return sorted(delays)
