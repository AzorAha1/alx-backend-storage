#!/usr/bin/env python3
"""using mongodb"""


def list_all(mongo_collection):
    """using python to list all documents in a collection

    Args:
        mongo_collection (list): list

    Returns:
        list: list of documents
    """
    if (mongo_collection.count_documents({}) == 0):
        return []
    documents = mongo_collection.find()
    return documents
