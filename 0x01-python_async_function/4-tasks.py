#!/usr/bin/env python3
"""
Executing multiple coroutines at the same
time with async
"""
import asyncio
from typing import List
from random import uniform
from asyncio import Task


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times
    with the specified max_delay.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
