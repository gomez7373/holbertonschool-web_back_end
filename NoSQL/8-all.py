#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    for school in list_all(school_collection):
        print("[{}] {}".format(school.get('_id'), school.get('name')))

