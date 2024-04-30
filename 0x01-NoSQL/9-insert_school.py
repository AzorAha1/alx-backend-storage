#!/usr/bin/env python3
"""insert into collection"""


def insert_school(mongo_collection, **kwargs):
    """inserting into school collection

    Args:
        mongo_collection (_type_): _description_

    Returns:
        _type_: _description_
    """
    theresult = mongo_collection.insert_one(kwargs)
    return theresult.inserted_id
