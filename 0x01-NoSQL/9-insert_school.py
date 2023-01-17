#!/usr/bin/env python3
""" Insert school module """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    my_list = []
    for key, value in kwargs.items():
        my_list.append({ key: value })
    mongo_collection.insert_many(my_list)
    x = mongo_collection.inserted_id
    return x
