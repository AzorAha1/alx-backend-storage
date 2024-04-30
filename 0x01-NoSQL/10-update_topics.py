#!/usr/bin/env python3
"""using pymongo"""


def update_topics(mongo_collection, name, topics):
    """updating database with new topics

    Args:
        mongo_collection (string): this is the collection in database
        name (string): name we want to modify the document of 
        topics (list): list of added topics

    Returns:
        list: newtopic(s) added
    """
    newtopics = mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
    return newtopics
    