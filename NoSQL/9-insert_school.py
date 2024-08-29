#!/usr/bin/env python3
""" pymongo list """

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ it will list all elements in a collection """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id