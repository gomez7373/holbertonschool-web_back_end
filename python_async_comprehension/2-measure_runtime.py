#!/usr/bin/env python3
import asyncio  # Import asyncio for asynchronous programming
import time     # Import time to measure the runtime of the function
from 1-async_comprehension import async_comprehension  # Import async_comprehension from the previous task


# Define an asynchronous function to measure the runtime
async def measure_runtime() -> float:
    start_time = time.perf_counter()  # Record the start time
    
    # Run 4 instances of async_comprehension in parallel using asyncio.gather
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    
    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time    # Return the total time taken
