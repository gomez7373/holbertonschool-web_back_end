#!/usr/bin/env python3
""" pymongo list """

import pymongo


def list_all(mongo_collection):
    """ it will list all elements in a collection """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())