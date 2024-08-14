#!/usr/bin/env python3
"""
Module for running multiple asyncio.Tasks concurrently using task_wait_random.
"""

import asyncio
from typing import List


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The created asyncio.Task object.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay
    and return the list of delays in ascending order.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
