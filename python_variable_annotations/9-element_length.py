#!/usr/bin/env python3
"""
Module for annotating a function that returns a list of tuples
with each element and its length.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples, where each tuple contains an element from the list
    and its length.

    Args:
        lst (Iterable[Sequence]): A list of sequences
        (like strings, lists, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where
        each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
