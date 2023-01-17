#!/usr/bin/env python3
""" Update topics module """
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    query: dict = {'name': name}
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
