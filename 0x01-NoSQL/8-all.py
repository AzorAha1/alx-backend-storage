#!/usr/bin/env python3
"""using mongodb"""


def list_all(mongo_collection):
    """using python to list all documents in a collection

    Args:
        mongo_collection (list): list

    Returns:
        list: list of documents
    """
    documents = []
    if (mongo_collection.count_documents({}) == 0):
        return document
    for document in mongo_collection.find():
        documents.append(document)
    return documents


if __name__ == '__main__':
    pass
