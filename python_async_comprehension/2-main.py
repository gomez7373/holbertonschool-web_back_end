#!/usr/bin/env python3
"""
This module tests the measure_runtime function by running it
and printing its output.
"""

import asyncio

measure_runtime = __import__("2-measure_runtime").measure_runtime


async def main():
    """
    Runs the measure_runtime function and prints its output.
    """
    return await measure_runtime()


print(asyncio.run(main()))
