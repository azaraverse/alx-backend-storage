#!/usr/bin/env python3
"""Aggregation pipelines"""


def top_students(mongo_collection):
    """
    A function that uses aggregation pipeline to return sorted
    average scores of students.
    """
    top_students = mongo_collection.aggregate([
        {
            '$unwind': '$topics'
        },
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ])

    return top_students
