#!/usr/bin/env python3
import asyncio  # Import asyncio for asynchronous programming
import time     # Import time to measure the runtime of the function
import importlib  # Import the importlib module to handle dynamic imports

# Dynamically import the async_comprehension function from the 1-async_comprehension module
# Using importlib allows us to import a module with a non-standard name
async_comprehension = importlib.import_module('1-async_comprehension').async_comprehension

# Define an asynchronous function to measure the runtime
async def measure_runtime() -> float:
    """
    Measures the total runtime required to execute async_comprehension
    four times in parallel.

    Returns:
        float: The total time taken to complete the four asynchronous tasks.
    """
    start_time = time.perf_counter()  # Record the start time using a high-resolution timer

    # Run 4 instances of async_comprehension in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time    # Return the total time taken
