#!/usr/bin/env python3
""""""
from pymongo import MongoClient


def log_stats(collection):
    """"""
    logs_count = collection.count_documents({})
    print(f'{logs_count} logs')


if __name__ == '__main__':
    """"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    log_stats(collection=collection)
