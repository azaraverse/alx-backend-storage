#!/usr/bin/env python3
"""Find a match"""


def schools_by_topic(mongo_collection, topic):
    """
    A function that returns a list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search
    """
    return mongo_collection.find({'topics': {'$eq': topic}})
