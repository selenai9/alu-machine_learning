#!/usr/bin/env python3
"""
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def count(collection, query):
    """Count documents, supporting old and new pymongo versions"""
    try:
        return collection.count_documents(query)
    except AttributeError:
        return collection.count(query)


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = count(collection, {})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {m: count(collection, {"method": m}) for m in methods}

    status_check = count(collection, {"method": "GET", "path": "/status"})

    print("{} logs".format(total_logs))
    print("Methods:")
    for m in methods:
        print("\tmethod {}: {}".format(m, method_counts[m]))
    print("{} status check".format(status_check))
