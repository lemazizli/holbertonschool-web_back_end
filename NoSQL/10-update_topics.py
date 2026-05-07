#!/usr/bin/env python3
"""Module to update school topics in a MongoDB collection."""


def update_topics(mongo_collection, name, topics):
    """Update topics of all school documents matching a given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
