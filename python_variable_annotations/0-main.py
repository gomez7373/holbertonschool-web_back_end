#!/usr/bin/env python3
"""
Module for adding two floats together.

This module provides a function to add two
floating-point numbers and return their sum.
"""
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

