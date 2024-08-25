#!/usr/bin/env python3
"""
This module tests the async_comprehension function by running it
and printing its output.
"""

import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def main():
    """
    Runs the async_comprehension function and prints its output.
    """
    print(await async_comprehension())


asyncio.run(main())
