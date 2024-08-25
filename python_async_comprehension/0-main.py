#!/usr/bin/env python3
"""
This module tests the async_generator function by collecting
and printing its yielded values.
"""

import asyncio

async_generator = __import__("0-async_generator").async_generator


async def print_yielded_values():
    """
    Collects and prints the values yielded by async_generator.
    """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)


asyncio.run(print_yielded_values())
