#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random
floating-point numbers between 0 and 10.
"""

import asyncio  # Import asyncio for asynchronous programming
import random   # Import random to generate random numbers
from typing import AsyncGenerator  # Import typing for type annotations


# Define an asynchronous generator function
async def async_generator() -> AsyncGenerator[float, None]:
    
    
    """
    Asynchronously generates and yields 10 random numbers between 0 and 10,
    with a 1-second delay between each number.
    
    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):              # Loop 10 times
        await asyncio.sleep(1)       # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
