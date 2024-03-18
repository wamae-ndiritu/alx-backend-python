#!/usr/bin/env python3
"""
Defines a basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Sleep for a random delay between 0
    and the specified max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
