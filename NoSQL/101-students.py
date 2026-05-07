#!/usr/bin/env python3
"""Module to retrieve students sorted by average score."""


def top_students(mongo_collection):
    """Return students sorted by average score with averageScore added."""
    result = mongo_collection.aggregate([
        {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
    return list(result)
