#!/usr/bin/env python3
""" Insert school module """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    for key, value in kwargs.items():
        mongo_collection.insert_one({key: value})
        x = mongo_collection.getId.find()
    return x
