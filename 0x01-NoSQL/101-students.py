#!/usr/bin/env python3
""""""


def top_students(mongo_collection):
    """"""
    top_students = mongo_collection.aggregate([
        {
            '$group': {'_id': '$_id', 'name': {'$first':'$name'}, 'averageScore': {'$avg': '$score'}}
        },
        {
            '$sort': {'averageScore': -1}
        }
    ])

    return top_students
