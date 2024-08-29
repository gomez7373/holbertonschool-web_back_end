#!/usr/bin/env python3
"""This module lists all documents in a collection"""


def list_all(mongo_collection):
    """
    this function lists all documents in a collection.
    """
    return list(mongo_collection.find()) or []