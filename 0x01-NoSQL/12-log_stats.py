#!/usr/bin/env python3
""""""
from pymongo import MongoClient


def log_stats(collection):
    """"""
    logs_count = collection.count_documents({})
    print(f'{logs_count} logs')

    # get method document count
    get_count = collection.count_documents({'method': {'$eq': 'GET'}})
    post_count = collection.count_documents({'method': {'$eq': 'POST'}})
    put_count = collection.count_documents({'method': {'$eq': 'PUT'}})
    patch_count = collection.count_documents({'method': {'$eq': 'PATCH'}})
    delete_count = collection.count_documents({'method': {'$eq': 'DELETE'}})
    print('Methods:')
    print(f'\tmethod GET: {get_count}')
    print(f'\tmethod POST: {post_count}')
    print(f'\tmethod PUT: {put_count}')
    print(f'\tmethod PATCH: {patch_count}')
    print(f'\tmethod DELETE: {delete_count}')


if __name__ == '__main__':
    """"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    log_stats(collection=collection)
