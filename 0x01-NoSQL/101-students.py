#!/usr/bin/env python3
""""""


def top_students(mongo_collection):
    """"""
    top_students = mongo_collection.aggregate([
        {
            '$unwind': '$topics'
        },
        {
            '$group': {'_id': '$_id', 'name': {'$first':'$name'}, 'averageScore': {'$avg': '$topics.score'}}
        },
        {
            '$sort': {'averageScore': -1}
        }
    ])

    return top_students
