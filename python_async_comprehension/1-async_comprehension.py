#!/usr/bin/env python3
from typing import List  # Import typing for type annotations
from 0-async_generator import async_generator  # Import async_generator from the previous task


# Define an asynchronous function that collects 10 random numbers
async def async_comprehension() -> List[float]:
    # Use an async comprehension to collect numbers from async_generator
    return [number async for number in async_generator()]
