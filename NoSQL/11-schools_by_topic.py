#!/usr/bin/env python3
"""Module to retrieve schools by topic from a MongoDB collection."""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
