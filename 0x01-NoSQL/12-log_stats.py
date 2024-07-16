#!/usr/bin/env python3
"""
A Python script that provides some stats about Nginx logs stored in
MongoDB
"""
from pymongo import MongoClient


def log_stats(collection):
    """Displays statistics about Nginx logs stored in MongoDB"""
    logs_count: int = collection.count_documents({})
    print(f'{logs_count} logs')

    # method document count
    get_count: int = collection.count_documents(
        {'method': {'$eq': 'GET'}}
    )
    post_count: int = collection.count_documents(
        {'method': {'$eq': 'POST'}}
    )
    put_count: int = collection.count_documents(
        {'method': {'$eq': 'PUT'}}
    )
    patch_count: int = collection.count_documents(
        {'method': {'$eq': 'PATCH'}}
    )
    delete_count: int = collection.count_documents(
        {'method': {'$eq': 'DELETE'}}
    )
    print('Methods:')
    print(f'\tmethod GET: {get_count}')
    print(f'\tmethod POST: {post_count}')
    print(f'\tmethod PUT: {put_count}')
    print(f'\tmethod PATCH: {patch_count}')
    print(f'\tmethod DELETE: {delete_count}')

    method_path: int = collection.count_documents(
        {'path': {'$eq': '/status'}}
    )
    print(f'{method_path} status check')


if __name__ == '__main__':
    """Run client"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    log_stats(collection=collection)
