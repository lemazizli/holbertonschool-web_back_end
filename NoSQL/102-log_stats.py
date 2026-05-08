#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def get_database():
    """Return the nginx collection from the logs database."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx
    return db


if __name__ == "__main__":
    db = get_database()
    print(str(db.count_documents({})) + " logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        nb_of_log = db.count_documents({"method": method})
        print("\tmethod " + method + ": " + str(nb_of_log))
    nb_of_doc = db.count_documents({"method": "GET", "path": "/status"})
    print(str(nb_of_doc) + " status check")
    doc_ip = [
        {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
        {"$sort": {"total": -1, "_id": -1}},
        {"$limit": 10}
    ]
    result = db.aggregate(doc_ip)
    print("IPs:")
    for ip in result:
        print("\t" + ip["_id"] + ": " + str(ip["total"]))
