#!/usr/bin/env python3
"""
Module for measuring the runtime of the wait_n function.
"""

import time
import asyncio
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay),
    and return the average time per task.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        float: The average time per task.
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
