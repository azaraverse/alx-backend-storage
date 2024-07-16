#!/usr/bin/env python3
"""A python function that lists all documents in a MongoDB collection"""
from typing import List

def list_all(mongo_collection) -> List:
    """
    This function lists all documents in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object
    Returns:
        List: A list of documents in a collection
    """
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
