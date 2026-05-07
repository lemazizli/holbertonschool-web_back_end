#!/usr/bin/env python3
"""Module that provides a function to insert a document
into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a MongoDB collection
    and return its new ID."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
