#!/usr/bin/env python3
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object to list documents from.

    Returns:
        list: A list of all documents in the collection. Returns an empty list if no documents are found.
    """
    return list(mongo_collection.find()) or []
