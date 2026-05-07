#!/usr/bin/env python3
"""Module de gestion des utilisateurs MongoDB."""


def list_all(mongo_collection):
    """Module that provides a function to list all documents
    in a MongoDB collection."""
    return list(mongo_collection.find())
