#!/usr/bin/env python3
"""
Module for creating a tuple from a string and a squared int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is a string
    and the second element is the square of an int or float.

    Args:
        k (str): The string.
        v (Union[int, float]): The number to be squared.

    Returns:
        Tuple[str, float]: A tuple with the string and the
        squared value as a float.
    """
    return (k, float(v ** 2))
