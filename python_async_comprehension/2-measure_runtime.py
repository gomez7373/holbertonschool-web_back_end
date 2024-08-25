#!/usr/bin/env python3
"""
This module measures the runtime of the async_comprehension function
when executed four times in parallel.
"""

import asyncio  # Import asyncio for asynchronous programming
import time  # Import time to measure the runtime of the function
import importlib  # Import the importlib module to handle dynamic imports

# Import the async_comprehension function dynamically
async_comprehension = importlib.import_module("1-async_comprehension") \
    .async_comprehension


# Define an asynchronous function to measure the runtime
async def measure_runtime() -> float:
    """
    Measures the total runtime required to execute async_comprehension
    four times in parallel.

    Returns:
        float: The total time taken to complete the four asynchronous tasks.
    """
    start_time = time.perf_counter()  # Record the start time

    # Execute async_comprehension 4 times in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time  # Return the total time taken
