#!/usr/bin/env python3
"""Change all topics of a school document"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """
    A function that changes all topics of a school document based
    on name

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics: [str]: list of topics taught by the school
    """
    return mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
