#!/usr/bin/env python3
"""A function that inserts a new document"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        kwargs: key-worded arguments
    Returns:
        Object: The new _id object
    """
    mongo_collection.insert_one(kwargs)
    return mongo_collection.inserted_id
