#!/usr/bin/env python3
"""
Module for computing the floor of a float.

This module provides a function to compute
the floor of a floating-point number and return it as an integer.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The floor of the float as an integer.
    """
    return math.floor(n)
