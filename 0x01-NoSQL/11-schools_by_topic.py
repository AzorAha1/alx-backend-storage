#!/usr/bin/env python3
"""using pymongo"""


def schools_by_topic(mongo_collection, topic):
    """filter schhols by topic

    Args:
        mongo_collection (string): collection
        topic (string): topic to filter

    Returns:
        list: list of filtered topics
    """
    filtered_topic = mongo_collection.find({"topics": topic})
    return filtered_topic
